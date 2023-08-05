VERSION = '0.0.6'

import re, traceback, logging
from .builder import LiquidLine, LiquidCode
from .exception import LiquidSyntaxError, LiquidRenderError
from .filters import filters

class Liquid(object):

	"""
	Implement liquid

	@static variable
	`DEBUG`: The debug flag. Default: False
	`MODE` : The mode of the template. Default: loose
	"""
	COMPLIED_RENDERED_STR = '_liquid_rendered_str'
	COMPLIED_RENDERED     = '_liquid_rendered'
	COMPLIED_CAPTURED     = '_liquid_captured'
	COMPLIED_RR_APPEND    = '_liquid_ret_append'
	COMPLIED_RR_EXTEND    = '_liquid_ret_extend'
	COMPLIED_CP_APPEND    = '_liquid_cap_append'
	COMPLIED_CP_EXTEND    = '_liquid_cap_extend'
	COMPLIED_FILTERS      = '_liquid_filters'

	TOKEN_LITERAL         = ''
	TOKEN_EXPR            = '{{}}'
	TOKEN_COMMENTTAG      = '{##}'
	TOKEN_ELIF            = 'elif'
	TOKEN_ELSE            = 'else'
	TOKEN_WHEN            = 'when'
	TOKEN_BREAK           = 'break'
	TOKEN_CONTINUE        = 'continue'
	TOKEN_ASSIGN          = 'assign'
	TOKEN_INCREMENT       = 'increment'
	TOKEN_DECREMENT       = 'decrement'
	TOKEN_PYTHON          = 'python'
	TOKEN_IF              = 'if'
	TOKEN_ENDIF           = 'endif'
	TOKEN_FOR             = 'for'
	TOKEN_ENDFOR          = 'endfor'
	TOKEN_UNLESS          = 'unless'
	TOKEN_ENDUNLESS       = 'endunless'
	TOKEN_CASE            = 'case'
	TOKEN_ENDCASE         = 'endcase'
	TOKEN_COMMENT         = 'comment'
	TOKEN_ENDCOMMENT      = 'endcomment'
	TOKEN_RAW             = 'raw'
	TOKEN_ENDRAW          = 'endraw'
	TOKEN_CAPTURE         = 'capture'
	TOKEN_ENDCAPTURE      = 'endcapture'
	TOKEN_WHILE           = 'while'
	TOKEN_ENDWHILE        = 'endwhile'

	REGEX_MODE = r'{%\s*mode\s+(.+?)%}\s*'

	DEBUG = False
	MODE  = 'loose'

	def __init__(self, text, **envs):
		"""
		Construct a Templite with the given `text`.
		`context` is a dictionary for future renderings.
		@params:
			`text`     : The template text
			`**envs`: The context used to render.
		"""
		self.logger = logging.getLogger(self.__class__.__name__)
		for handler in self.logger.handlers:
			handler.close()
		del self.logger.handlers[:]
		handler = logging.StreamHandler()
		handler.setFormatter(logging.Formatter('[%(asctime)s Liquid] %(message)s', '%Y-%m-%d %H:%M:%S'))
		self.logger.addHandler(handler)
		#self.logger.setLevel(Liquid.LOGLEVEL)

		self.envs  = {
			Liquid.COMPLIED_FILTERS: filters,
			'true'                 : True,
			'false'                : False,
			'nil'                  : None
		}
		self.envs.update(envs)
		self.text     = text
		self.buffered = []
		self.captured = []

		#lines2    = self.text.split('\n', 1)
		#modematch = re.match(r'^\s*{%\s*mode\s+(.+)%}\s*$', lines2[0])
		# mode now can be anywhere
		modematch = re.search(Liquid.REGEX_MODE, self.text)

		mode  = Liquid.MODE
		self.debug = Liquid.DEBUG
		if modematch:
			self.text = re.sub(Liquid.REGEX_MODE, '', self.text)
			mm = modematch.group(1)
			if 'nodebug' in mm:   self.debug = False
			elif 'debug' in mm:   self.debug = True
			if 'loose' in mm:     mode = 'loose'
			elif 'mixed' in mm:   mode = 'mixed'
			elif 'compact' in mm: mode = 'compact'

		self.logger.setLevel(logging.DEBUG if self.debug else logging.CRITICAL)
		self.logger.debug('Mode: {} {}'.format(mode, 'debug' if self.debug else ''))

		# We construct a function in source form, then compile it and hold onto
		# it, and execute it to render the template.
		self.code = LiquidCode()

		self.code.addLine("{} = []".format(Liquid.COMPLIED_RENDERED))
		self.code.addLine("{} = []".format(Liquid.COMPLIED_CAPTURED))
		self.code.addLine("{} = {}.append".format(Liquid.COMPLIED_RR_APPEND, Liquid.COMPLIED_RENDERED))
		self.code.addLine("{} = {}.extend".format(Liquid.COMPLIED_RR_EXTEND, Liquid.COMPLIED_RENDERED))
		self.code.addLine("{} = {}.append".format(Liquid.COMPLIED_CP_APPEND, Liquid.COMPLIED_CAPTURED))
		self.code.addLine("{} = {}.extend".format(Liquid.COMPLIED_CP_EXTEND, Liquid.COMPLIED_CAPTURED))

		opsStack = []

		# Split the text to a list of tokens.
		if mode == 'compact':
			tokens   = re.split(r"(?s)([ \t]*{{-?.*?-?}}[ \t]*\n?|[ \t]*{%-?.*?-?%}[ \t]*\n?|[ \t]*{#-?.*?-?#}[ \t]*\n?)", self.text)
		elif mode == 'mixed':
			tokens   = re.split(r"(?s)({{.*?}}|[ \t]*{%-?.*?-?%}[ \t]*\n?|[ \t]*{#-?.*?-?#}[ \t]*\n?)", self.text)
		else:
			tokens   = re.split(r"(?s)([ \t]*{{-.*?-}}[ \t]*\n?|{{.*?}}|[ \t]*{%-.*?-%}[ \t]*\n?|{%.*?%}|[ \t]*{#-.*?-#}[ \t]*\n?|{#.*?#})", self.text)
		lineno   = 1
		literals = []
		for token in tokens:
			if not token:
				continue
			tokentype, neattoken = Liquid._tokenType(token, lineno, opsStack)
			self.logger.debug('Token type: {!r}, content: {!r} at line {}: {!r}'.format(tokentype, neattoken, lineno, token))
			if not opsStack or opsStack[-1][0] not in [Liquid.TOKEN_RAW, Liquid.TOKEN_COMMENT]:
				if tokentype in [Liquid.TOKEN_IF, Liquid.TOKEN_FOR, Liquid.TOKEN_WHILE]:
					self._flush(capname = Liquid._capname(opsStack))
					self._parsePythonLiteral(tokentype, neattoken, lineno = lineno, src = token, indent = True)
					opsStack.append((tokentype, ))
				elif tokentype in [Liquid.TOKEN_BREAK, Liquid.TOKEN_CONTINUE]:
					if not opsStack or not any([op[0] in [Liquid.TOKEN_FOR, Liquid.TOKEN_WHILE] for op in opsStack]):
						raise LiquidSyntaxError('"{}" must be in a loop block'.format(tokentype), lineno, token)
					self._flush(capname = Liquid._capname(opsStack))
					self._parsePythonLiteral(tokentype, neattoken, lineno = lineno, src = token, colon = False)
				elif tokentype == Liquid.TOKEN_PYTHON:
					self._flush(capname = Liquid._capname(opsStack))
					self._parsePythonLiteral(neattoken, lineno = lineno, src = token, colon = False)
				elif tokentype == Liquid.TOKEN_ELIF:
					if not opsStack or not any([op[0] in [Liquid.TOKEN_IF, Liquid.TOKEN_UNLESS] for op in opsStack]):
						raise LiquidSyntaxError('"{}" must be in an if/unless block'.format(tokentype), lineno, token)
					self._flush(capname = Liquid._capname(opsStack))
					self._parsePythonLiteral(tokentype, neattoken, lineno = lineno, src = token, indent = True, dedent = True)
				elif tokentype == Liquid.TOKEN_ELSE:
					if not opsStack or not any([op[0] in [Liquid.TOKEN_IF, Liquid.TOKEN_UNLESS, Liquid.TOKEN_CASE] for op in opsStack]):
						raise LiquidSyntaxError('"{}" must be in an if/unless/case block'.format(tokentype), lineno, token)
					self._flush(capname = Liquid._capname(opsStack))
					self._parsePythonLiteral(tokentype, neattoken, lineno = lineno, src = token, indent = True, dedent = True)
				elif tokentype == Liquid.TOKEN_COMMENTTAG:
					self._flush(capname = Liquid._capname(opsStack))
				elif tokentype == Liquid.TOKEN_CAPTURE:
					self._flush(capname = Liquid._capname(opsStack))
					opsStack.append((tokentype, neattoken))
				elif tokentype == Liquid.TOKEN_ENDCAPTURE:
					if not opsStack or opsStack[-1][0] != Liquid.TOKEN_CAPTURE:
						raise LiquidSyntaxError('Unmatched tag: {}/{}'.format(opsStack[-1][0] if opsStack else '', tokentype), lineno, token)
					self._flush(capname = opsStack[-1][1])
					self.code.addLine('{} = "".join(str(x) for x in {})'.format(opsStack[-1][-1], Liquid.COMPLIED_CAPTURED))
					self.code.addLine('del {}[:]'.format(Liquid.COMPLIED_CAPTURED))
					opsStack.pop(-1)
				elif tokentype == Liquid.TOKEN_EXPR:
					self._parseExpr(neattoken, lineno, token, capture = Liquid._capname(opsStack))
				elif tokentype == Liquid.TOKEN_CASE:
					self._flush(capname = Liquid._capname(opsStack))
					opsStack.append((tokentype, (neattoken, lineno, token)))
				elif tokentype == Liquid.TOKEN_WHEN:
					if not opsStack or opsStack[-1][0] != Liquid.TOKEN_CASE:
						raise LiquidSyntaxError('No case opened for "when"', lineno, token)
					self._flush(capname = Liquid._capname(opsStack))
					if len(opsStack[-1]) == 2:
						self._parseWhen(opsStack[-1][1], neattoken, lineno, token, started = False)
						opsStack[-1] += (None, )
					else:
						self._parseWhen(opsStack[-1][1], neattoken, lineno, token, started = True)
				elif tokentype == Liquid.TOKEN_ASSIGN:
					self._flush(capname = Liquid._capname(opsStack))
					self._parseAssign(neattoken, lineno, token)
				elif tokentype == Liquid.TOKEN_INCREMENT:
					self._flush(capname = Liquid._capname(opsStack))
					self._parseIncrement(neattoken, lineno = lineno, src = token)
				elif tokentype == Liquid.TOKEN_DECREMENT:
					self._flush(capname = Liquid._capname(opsStack))
					self._parseDecrement(neattoken, lineno = lineno, src = token)
				elif tokentype == Liquid.TOKEN_UNLESS:
					self._flush(capname = Liquid._capname(opsStack))
					self._parseUnless(neattoken, lineno = lineno, src = token)
					opsStack.append((tokentype, neattoken))
				elif tokentype in [
					Liquid.TOKEN_ENDIF, Liquid.TOKEN_ENDFOR, Liquid.TOKEN_ENDWHILE,
					Liquid.TOKEN_ENDUNLESS, Liquid.TOKEN_ENDCASE, Liquid.TOKEN_IF,
					Liquid.TOKEN_FOR, Liquid.TOKEN_WHILE]:
					if not opsStack or opsStack[-1][0] != tokentype[3:]:
						raise LiquidSyntaxError('Unmatched tag: {}/{}'.format(opsStack[-1][0] if opsStack else '', tokentype), lineno, token)
					self._flush(capname = Liquid._capname(opsStack))
					opsStack.pop(-1)
					self.code.dedent()
				elif tokentype in [Liquid.TOKEN_COMMENT, Liquid.TOKEN_RAW]:
					self._flush(capname = Liquid._capname(opsStack))
					opsStack.append((tokentype, neattoken))
				else:
					self._parseLiteral(token, capture = Liquid._capname(opsStack))

			else: # raw/comment started
				if opsStack[-1][0] == Liquid.TOKEN_COMMENT and tokentype == Liquid.TOKEN_ENDCOMMENT:
					self._flush(capname = Liquid._capname(opsStack))
					self._parseComment(literals, sign = opsStack[-1][1], capture = Liquid._capname(opsStack))
					literals = []
					opsStack.pop(-1)
				elif opsStack[-1][0] == Liquid.TOKEN_RAW and tokentype == Liquid.TOKEN_ENDRAW:
					self._flush(capname = Liquid._capname(opsStack))
					self._parseRaw(literals, capture = Liquid._capname(opsStack))
					literals = []
					opsStack.pop(-1)
				else:
					literals.append(token)
			lineno += token.count('\n')

		if opsStack:
			raise LiquidSyntaxError(msg = 'Unclosed template tag: {}'.format(opsStack[-1][0]))

		self._flush()

		self.code.addLine("{} = ''.join(str(x) for x in {})".format(Liquid.COMPLIED_RENDERED_STR, Liquid.COMPLIED_RENDERED))
		self.code.addLine("del {}".format(Liquid.COMPLIED_CAPTURED))
		self.code.addLine("del {}".format(Liquid.COMPLIED_CP_APPEND))
		self.code.addLine("del {}".format(Liquid.COMPLIED_CP_EXTEND))
		self.code.addLine("del {}".format(Liquid.COMPLIED_FILTERS))
		self.code.addLine("del {}".format(Liquid.COMPLIED_RENDERED))
		self.code.addLine("del {}".format(Liquid.COMPLIED_RR_APPEND))
		self.code.addLine("del {}".format(Liquid.COMPLIED_RR_EXTEND))

		self.logger.debug('Python source:')
		self.logger.debug('-' * 80)

		if self.debug:
			import math
			nlines = len(self.code.codes)
			nbit   = int(math.log(nlines, 10)) + 3
			for i, line in enumerate(self.code.codes):
				self.logger.debug((str(i+1) + '.').ljust(nbit) + str(line).rstrip())

	@staticmethod
	def _exprFilter(argstr, filterstr, lineno, src):
		argstup = '({})'.format(argstr)
		expand = chain = False
		if filterstr.startswith('*'):
			expand = True
			filterstr = filterstr[1:]
		if filterstr.startswith('&'):
			chain  = True
			filterstr = filterstr[1:]

		if filterstr.startswith('@'):
			# liquid filters, now need to start with @
			# see https://shopify.github.io/liquid/filters/abs/
			filterstr = filterstr[1:]
			tmp = Liquid.split(filterstr, ':', limit = 1)
			func, arg = tmp if len(tmp) == 2 else (tmp[0], None)
			if func not in filters:
				raise LiquidSyntaxError('Unknown liquid filter: @{}'.format(filterstr), lineno, src)
			# {{ x | @filter }} => filter(x)
			# {{ x | @filter: a }} => filter(x, a)
			# {{ x, y | *@filter: a }} => filter(x, y, a)
			# {{ x, y | @filter: a }} => filter((x, y), a)
			# {{ x, y | *&@filter: a }} => (x, y, filter(x, y, a))
			# {{ x, y | &@filter: a }} => (x, y, filter((x, y), a))
			ret = '{}[{!r}]({}{})'.format(
				Liquid.COMPLIED_FILTERS,
				func,
				argstr if expand else argstup,
				', {}'.format(arg) if arg else ''
			)
		elif filterstr.startswith('.'):
			# attributes
			filterstr = filterstr[1:]
			tmp = Liquid.split(filterstr, ':', limit = 1)
			func, arg = tmp if len(tmp) == 2 else (tmp[0], None)
			# {{ x | .__file__}} => x.__file__
			# {{ x | .join(["a", "b"]) }} => x.join(["a", "b"])
			# {{ x | .join: ["a", "b"]}} => x.join(["a", "b"])
			# {{ x | &.attr }} => (x, x.attr)
			# {{ x, y | .count(1) }} => (x, y).count(1)
			# {{ x, y | .count: 1 }} => (x, y).count(1)
			# {{ x, y | *.join: ["a", "b"] }} => x.join(["a", "b"]) # y lost!!
			# {{ x, y | &.count:1 }} => (x, y, (x, y).count(1))
			# {{ x, y | *&.join: ["a", "b"] }} => (x, y, x.join(["a", "b"]))
			args = Liquid.split(argstr, ',', limit = 1)
			ret = '{}.{}{}'.format(
				args[0] if expand else argstup,
				func,
				'' if arg is None else '({})'.format(arg)
			)
		elif filterstr.startswith('['):
			# getitem
			tmp = Liquid.split(filterstr, ':', limit = 1)
			func, arg = tmp if len(tmp) == 2 else (tmp[0], None)
			# {{ x | [0] }} => x[0]
			# {{ x | &[0] }} => (x, x[0])
			# {{ x | [0](1) }} => x[0](1)
			# {{ x | [0]: 1 }} => x[0](1)
			# {{ x, y | [0] }} => (x, y)[0] == x
			# {{ x, y | &[0] }} => (x, y, (x, y)[0]) == (x, y, x)
			# {{ x, y | *[0] }} => x[0]
			# {{ x, y | *&[0] }} => (x, y, x[0])
			# {{ x, y | [0]: 1 }} => (x, y)[0](1)
			args = Liquid.split(argstr, ',', limit = 1)
			ret = '{}{}{}'.format(
				args[0] if expand else argstup,
				func,
				'' if arg is None else '({})'.format(arg)
			)
		elif filterstr.startswith(':'):
			# lambdas
			argnames = list('abcdefghijklmnopqrstuvwxyz')
			# {{ x | :a[1]}} => (lambda a: a[1])(x)
			# {{ x | &:a[1] }} => (x, (lambda a: a[1])(x))
			# {{ x, y | *:a+b }} => (lambda a, b: a+b)(x, y)
			# {{ x, y | :sum(a)}} => (lambda a: sum(a))((x, y))
			if expand:
				funcargs, args = ', '.join(argnames[:len(Liquid.split(argstr, ','))]), argstr
			else:
				funcargs, args = argnames[0], '({})'.format(argstr)
			ret = '(lambda {}{})({})'.format(funcargs, filterstr, args)
		elif filterstr.startswith('lambda'):
			# real lambda
			# {{ x | lambda a:a[1]}} => (lambda a: a[1])(x)
			# {{ x | &lambda a:a[1] }} => (x, (lambda a: a[1])(x))
			# {{ x, y | *lambda a, b: a+b }} => (lambda a, b: a+b)(x, y)
			# {{ x, y | lambda a:sum(a)}} => (lambda a: sum(a))((x, y))
			ret = '({})({})'.format(filterstr, argstr if expand else argstup)
		else:
			# {{ [1,2,3] | len }} => len([1,2,3])
			# {{ 1 | &isinstance:int }} => (1, isinstance(1, int)) => (1, True)
			# {{ x, y, z | &tuple }} => (x, y, z, (x, y, z))
			# {{ x, y, z | *&filter: w }} => (x, y, z, filter(x, y, z, w))
			# {{ x, y, z | *filter: w }} => filter(x, y, z, w)
			# {{ x, y, z | &filter: w }} => (x, y, z, filter((x, y, z), w)
			tmp = Liquid.split(filterstr, ':', limit = 1)
			func, arg = tmp if len(tmp) == 2 else (tmp[0], None)
			ret = '{}({}{})'.format(
				func,
				argstr if expand else argstup,
				', {}'.format(arg) if arg else ''
			)
		return '{}, {}'.format(argstr, ret) if chain else ret

	@staticmethod
	def _capname(opsStack):
		captags = [op[0] for op in opsStack if op[0] == Liquid.TOKEN_CAPTURE]
		if captags:
			return captags[-1][1]

	@staticmethod
	def _exprCode(code, lineno, src):
		pipes = Liquid.split(code, '|')
		vals  = pipes.pop(0)
		for pipe in pipes:
			vals = Liquid._exprFilter(vals, pipe, lineno, src)
		return '({})'.format(vals)

	@staticmethod
	def split (s, delimter, trim = True, limit = 0): # pragma: no cover
		"""
		Split a string using a single-character delimter
		@params:
			`s`: the string
			`delimter`: the single-character delimter
			`trim`: whether to trim each part. Default: True
		@examples:
			```python
			ret = split("'a,b',c", ",")
			# ret == ["'a,b'", "c"]
			# ',' inside quotes will be recognized.
			```
		@returns:
			The list of substrings
		"""
		ret   = []
		special1 = ['(', ')', '[', ']', '{', '}']
		special2 = ['\'', '"']
		special3 = '\\'
		flags1 = [0, 0, 0]
		flags2 = [False, False]
		flags3 = False
		start  = 0
		nlim   = 0
		for i, c in enumerate(s):
			if c == special3:
				# next char is escaped
				flags3 = not flags3
			elif not flags3:
				# no escape
				if c in special1:
					index = special1.index(c)
					if index % 2 == 0:
						flags1[int(index/2)] += 1
					else:
						flags1[int(index/2)] -= 1
				elif c in special2:
					index = special2.index(c)
					flags2[index] = not flags2[index]
				elif c == delimter and not any(flags1) and not any(flags2):
					r = s[start:i]
					if trim: r = r.strip()
					ret.append(r)
					start = i + 1
					nlim = nlim + 1
					if limit and nlim >= limit:
						break
			else:
				# escaping closed
				flags3 = False
		r = s[start:]
		if trim: r = r.strip()
		ret.append(r)
		return ret

	@staticmethod
	def _tokenType(token, lineno, opsStack):
		ops = [op[0] for op in opsStack] if opsStack else []

		neattoken = token.strip()
		tag3 = neattoken[:3] + neattoken[-3:]
		tag2 = neattoken[:2] + neattoken[-2:]
		istag = False
		if tag3 in ['{{--}}', '{%--%}', '{#--#}']:
			neattoken = neattoken[3:-3].strip()
			istag = True
		elif tag2 in ['{{}}', '{%%}', '{##}']:
			neattoken = neattoken[2:-2].strip()
			istag = True

		if istag:
			# raw/comment
			if Liquid.TOKEN_RAW in ops and (tag2[1] != '%' or neattoken != Liquid.TOKEN_ENDRAW):
				return Liquid.TOKEN_LITERAL, ''
			if Liquid.TOKEN_COMMENT in ops and (tag2[1] != '%' or neattoken != Liquid.TOKEN_ENDCOMMENT):
				return Liquid.TOKEN_LITERAL, ''

			if tag2[1] == '#':
				return Liquid.TOKEN_COMMENTTAG, ''
			elif tag2[1] == '{':
				return Liquid.TOKEN_EXPR, neattoken
			else:
				words = neattoken.split(None, 1)
				# sole keywords
				if words[0] in ['break', 'continue', 'raw']:
					if len(words) > 1:
						raise LiquidSyntaxError('Additional statements for "{}"'.format(words[0]), lineno, token)
					return getattr(Liquid, 'TOKEN_' + words[0].upper()), ''
				elif words[0] == 'comment':
					return Liquid.TOKEN_COMMENT, words[1] if len(words) > 1 else '#'
				elif words[0] in ['if', 'for', 'elif', 'elsif', 'elseif', 'unless', 'case', 'when', 'capture', 'while', 'python']:
					if len(words) == 1:
						raise LiquidSyntaxError('No statements for "{}"'.format(words[0]), lineno, token)
					if words[0] == 'elsif' or words[0] == 'elseif':
						words[0] = 'elif'
					return getattr(Liquid, 'TOKEN_' + words[0].upper()), words[1]
				elif words[0] == 'assign':
					if len(words) == 1:
						raise LiquidSyntaxError('No statements for "{}"'.format(words[0]), lineno, token)
					equals = words[1].split('=', 1)
					if len(equals) == 1:
						raise LiquidSyntaxError('Malformat assignment, no equal sign found: {}'.format(words[0]), lineno, token)
					return Liquid.TOKEN_ASSIGN, equals
				elif words[0] == 'else':
					if len(words) == 1:
						return Liquid.TOKEN_ELSE, ''
					parts = words[1].split(None, 1)
					if parts[0] != 'if':
						raise LiquidSyntaxError('"Else" must be followed by "if" statement if any', lineno, token)
					if len(parts) == 1:
						raise LiquidSyntaxError('No statements for "else if"', lineno, token)
					return Liquid.TOKEN_ELIF, parts[1]
				elif words[0] == 'increment' or words[0] == 'decrement':
					if len(words) == 1:
						raise LiquidSyntaxError('No variable for {}'.format(words[0]), lineno, token)
					return getattr(Liquid, 'TOKEN_' + words[0].upper()), words[1]
				elif words[0].startswith('end'):
					if len(words) > 1:
						raise LiquidSyntaxError('Additional statements for {}'.format(words[0]), lineno, token)
					endtype = words[0][3:]
					try:
						return getattr(Liquid, 'TOKEN_END' + endtype.upper()), ''
					except AttributeError:
						raise LiquidSyntaxError('Unknown end tag {}'.format(words[0]), lineno, token)

		return Liquid.TOKEN_LITERAL, token

	def _parseExpr(self, token, lineno, src, capture):
		self.logger.debug(' - parsing expression: {}'.format(token))
		container = self.captured if capture else self.buffered
		container.append(Liquid._exprCode(token, lineno, src))

	def _parsePythonLiteral(self, token, neattoken = '', lineno = 0, src = None, colon = True, indent = False, dedent = False):
		self.logger.debug(' - parsing python literal: {} {}'.format(token, neattoken))
		if dedent:
			self.code.dedent()
		src = src or token
		line = LiquidLine('{}{}{}'.format(
			token,
			' ' + neattoken if neattoken else ''
			, ':' if colon else ''), lineno = lineno, src = src)
		self.code.addLine(line)
		if indent:
			self.code.indent()

	def _parseWhen(self, casevar, whenvar, lineno, src, started):
		casevar = Liquid._exprCode(casevar[0], casevar[1], casevar[2])
		whenvar = Liquid._exprCode(whenvar, lineno, src)
		if started:
			self._parsePythonLiteral(
				Liquid.TOKEN_ELIF,
				'{} == {}'.format(casevar, whenvar),
				indent = True, dedent = True, lineno = lineno, src = src)
		else:
			self._parsePythonLiteral(
				Liquid.TOKEN_IF,
				'{} == {}'.format(casevar, whenvar),
				indent = True, dedent = False, lineno = lineno, src = src)

	def _parseUnless(self, neattoken, lineno, src):
		self.logger.debug(' - parsing unless: {}'.format(neattoken))
		self.code.addLine(LiquidLine('if not ({}):'.format(neattoken), lineno = lineno, src = src))
		self.code.indent()

	def _parseAssign(self, equals, lineno, src):
		self.code.addLine(LiquidLine('{} = {}'.format(equals[0], Liquid._exprCode(equals[1], lineno, src)), lineno = lineno, src = src))

	def _parseIncrement(self, var, lineno, src):
		self.code.addLine(LiquidLine('{} += 1'.format(var), lineno = lineno, src = src))

	def _parseDecrement(self, var, lineno, src):
		self.code.addLine(LiquidLine('{} -= 1'.format(var), lineno = lineno, src = src))

	def _parseComment(self, literals, sign, capture):
		self.logger.debug(' - parsing comment: {!r}'.format(literals))
		container = self.captured if capture else self.buffered
		container.extend([
			repr('{} {}'.format(sign, line.lstrip()))
			for line in ''.join(literals).splitlines(True)
		])

	def _parseRaw(self, literals, capture):
		self.logger.debug(' - parsing raw: {!r}'.format(literals))
		container = self.captured if capture else self.buffered
		container.append(repr(''.join(literals)))

	def _parseLiteral(self, token, capture):
		self.logger.debug(' - parsing literal: {!r}'.format(token))
		container = self.captured if capture else self.buffered
		container.append(repr(token))

	def _flush(self, capname = None):
		container = self.captured if capname else self.buffered
		if len(container) == 1:
			self.code.addLine("{}({})".format(
				Liquid.COMPLIED_CP_APPEND if capname else Liquid.COMPLIED_RR_APPEND,
				container[0]))
		elif len(container) > 1:
			self.code.addLine("{}([".format(
				Liquid.COMPLIED_CP_EXTEND if capname else Liquid.COMPLIED_RR_EXTEND))
			self.code.indent()
			for line in container:
				self.code.addLine(line + ',')
			self.code.dedent()
			self.code.addLine("])")
		del container[:]

	def render(self, **context):
		"""
		Render this template by applying it to `context`.
		@params:
			`context`: a dictionary of values to use in this rendering.
		@returns:
			The rendered string
		"""
		# Make the complete context we'll use.
		localns = self.envs.copy()
		localns.update(context)

		try:
			exec(str(self.code), None, localns)
			return localns[Liquid.COMPLIED_RENDERED_STR]
		except Exception:
			stacks = list(reversed(traceback.format_exc().splitlines()))
			for stack in stacks:
				stack = stack.strip()
				if stack.startswith('File "<string>"'):
					lineno = int(stack.split(', ')[1].split()[-1])
					source = []
					if 'NameError:' in stacks[0]:
						source.append('Do you forget to provide the data?')

					import math
					source.append('\nCompiled source (use debug mode to see full source):')
					source.append('---------------------------------------------------')
					nlines = len(self.code.codes)
					nbit   = int(math.log(nlines, 10)) + 3
					for i, line in enumerate(self.code.codes):
						if i - 7 > lineno or i + 9 < lineno: continue
						if i + 1 != lineno:
							source.append('  ' + (str(i+1) + '.').ljust(nbit) + str(line).rstrip())
						else:
							source.append('* ' + (str(i+1) + '.').ljust(nbit) + str(line).rstrip())

					raise LiquidRenderError(
						stacks[0],
						repr(self.code.codes[lineno - 1]) +
						'\n' + '\n'.join(source) +
						'\n\nPREVIOUS EXCEPTION:\n------------------\n' +
						'\n'.join(stacks) + '\n' +
						'\nCONTEXT:\n------------------\n' +
						'\n'.join(
							'  ' + key + ': ' + str(val)
							for key, val in localns.items() if not key.startswith('_liquid_') and not key.startswith('__')
						) + '\n'
					)
			raise # pragma: no cover
