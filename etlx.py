
# python wrapper for package github.com/realdatadriven/etlx within overall package etlx
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy gen github.com/realdatadriven/etlx

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _etlx
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from etlx import etlx
# and then refer to everything using etlx. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice []interface{}
class Slice_interface_(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.Slice_interface__CTor()
			_etlx.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_interface_.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		s = 'etlx.Slice_interface_ len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'etlx.Slice_interface_([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _etlx.Slice_interface__len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _etlx.Slice_interface__len(self.handle)
				return Slice_interface_(handle=_etlx.Slice_interface__subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return _etlx.Slice_interface__elem(self.handle, key)
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_etlx.Slice_interface__set(self.handle, idx, value)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_interface_.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _etlx.Slice_interface__elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_etlx.Slice_interface__append(self.handle, value)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []map[string]any
class Slice_Map_string_any(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.Slice_Map_string_any_CTor()
			_etlx.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_Map_string_any.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		s = 'etlx.Slice_Map_string_any len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'etlx.Slice_Map_string_any([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _etlx.Slice_Map_string_any_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _etlx.Slice_Map_string_any_len(self.handle)
				return Slice_Map_string_any(handle=_etlx.Slice_Map_string_any_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Map_string_any(handle=_etlx.Slice_Map_string_any_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_etlx.Slice_Map_string_any_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_Map_string_any.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = Map_string_any(handle=_etlx.Slice_Map_string_any_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_etlx.Slice_Map_string_any_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []time.Time
class Slice_time_Time(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.Slice_time_Time_CTor()
			_etlx.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_time_Time.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		s = 'etlx.Slice_time_Time len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'etlx.Slice_time_Time([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _etlx.Slice_time_Time_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _etlx.Slice_time_Time_len(self.handle)
				return Slice_time_Time(handle=_etlx.Slice_time_Time_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.time_Time(handle=_etlx.Slice_time_Time_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_etlx.Slice_time_Time_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_time_Time.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = go.time_Time(handle=_etlx.Slice_time_Time_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_etlx.Slice_time_Time_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for map map[string]any
class Map_string_any(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.Map_string_any_CTor()
			_etlx.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Mapping):
					raise TypeError('Map_string_any.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_etlx.Map_string_any_set(self.handle, k, v)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		s = 'etlx.Map_string_any len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'etlx.Map_string_any({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _etlx.Map_string_any_len(self.handle)
	def __getitem__(self, key):
		return any(handle=_etlx.Map_string_any_elem(self.handle, key))
	def __setitem__(self, key, value):
		_etlx.Map_string_any_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _etlx.Map_string_any_delete(self.handle, key)
	def keys(self):
		return go.Slice_string(handle=_etlx.Map_string_any_keys(self.handle))
	def values(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append(self[k])
		return vls
	def items(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append((k, self[k]))
		return vls
	def __iter__(self):
		return iter(self.items())
	def __contains__(self, key):
		return _etlx.Map_string_any_contains(self.handle, key)

# Python type for map map[string]interface{}
class Map_string_interface_(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.Map_string_interface__CTor()
			_etlx.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Mapping):
					raise TypeError('Map_string_interface_.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_etlx.Map_string_interface__set(self.handle, k, v)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		s = 'etlx.Map_string_interface_ len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'etlx.Map_string_interface_({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _etlx.Map_string_interface__len(self.handle)
	def __getitem__(self, key):
		return _etlx.Map_string_interface__elem(self.handle, key)
	def __setitem__(self, key, value):
		_etlx.Map_string_interface__set(self.handle, key, value)
	def __delitem__(self, key):
		return _etlx.Map_string_interface__delete(self.handle, key)
	def keys(self):
		return go.Slice_string(handle=_etlx.Map_string_interface__keys(self.handle))
	def values(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append(self[k])
		return vls
	def items(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append((k, self[k]))
		return vls
	def __iter__(self):
		return iter(self.items())
	def __contains__(self, key):
		return _etlx.Map_string_interface__contains(self.handle, key)


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---

# Python type for interface db.DBInterface
class DBInterface(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = 0
	def Close(self):
		"""Close() str"""
		return _etlx.db_DBInterface_Close(self.handle)
	def ExecuteNamedQuery(self, query, data):
		"""ExecuteNamedQuery(str query, object data) int, str"""
		return _etlx.db_DBInterface_ExecuteNamedQuery(self.handle, query, data.handle)
	def ExecuteQuery(self, query, *args):
		"""ExecuteQuery(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_DBInterface_ExecuteQuery(self.handle, query, data.handle)
	def ExecuteQueryPGInsertWithLastInsertId(self, query, *args):
		"""ExecuteQueryPGInsertWithLastInsertId(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_DBInterface_ExecuteQueryPGInsertWithLastInsertId(self.handle, query, data.handle)
	def ExecuteQueryRowsAffected(self, query, *args):
		"""ExecuteQueryRowsAffected(str query, []str data) long, str"""
		data = Slice_interface_(args)
		return _etlx.db_DBInterface_ExecuteQueryRowsAffected(self.handle, query, data.handle)
	def GetDriverName(self):
		"""GetDriverName() str"""
		return _etlx.db_DBInterface_GetDriverName(self.handle)
	def IsEmpty(self, value):
		"""IsEmpty(str value) bool"""
		return _etlx.db_DBInterface_IsEmpty(self.handle, value)
	def Ping(self):
		"""Ping() str"""
		return _etlx.db_DBInterface_Ping(self.handle)
	def Query2CSV(self, query, csv_path, *args):
		"""Query2CSV(str query, str csv_path, []str params) bool, str"""
		params = Slice_interface_(args)
		return _etlx.db_DBInterface_Query2CSV(self.handle, query, csv_path, params.handle)


# ---- Structs ---

# Python type for struct db.DB
class DB(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.db_DB_CTor()
			_etlx.IncRef(self.handle)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'db.DB{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'db.DB ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def GetDriverName(self):
		"""GetDriverName() str"""
		return _etlx.db_DB_GetDriverName(self.handle)
	def ExecuteQuery(self, query, *args):
		"""ExecuteQuery(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_DB_ExecuteQuery(self.handle, query, data.handle)
	def ExecuteQueryPGInsertWithLastInsertId(self, query, *args):
		"""ExecuteQueryPGInsertWithLastInsertId(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_DB_ExecuteQueryPGInsertWithLastInsertId(self.handle, query, data.handle)
	def ExecuteQueryRowsAffected(self, query, *args):
		"""ExecuteQueryRowsAffected(str query, []str data) long, str"""
		data = Slice_interface_(args)
		return _etlx.db_DB_ExecuteQueryRowsAffected(self.handle, query, data.handle)
	def ExecuteNamedQuery(self, query, data):
		"""ExecuteNamedQuery(str query, object data) int, str"""
		return _etlx.db_DB_ExecuteNamedQuery(self.handle, query, data.handle)
	def IsEmpty(self, value):
		"""IsEmpty(str value) bool"""
		return _etlx.db_DB_IsEmpty(self.handle, value)
	def Query2CSV(self, query, csv_path, *args):
		"""Query2CSV(str query, str csv_path, []str params) bool, str"""
		params = Slice_interface_(args)
		return _etlx.db_DB_Query2CSV(self.handle, query, csv_path, params.handle)

# Python type for struct db.DuckDB
class DuckDB(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.db_DuckDB_CTor()
			_etlx.IncRef(self.handle)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'db.DuckDB{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'db.DuckDB ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def ExecuteQuery(self, query, *args):
		"""ExecuteQuery(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_DuckDB_ExecuteQuery(self.handle, query, data.handle)
	def ExecuteQueryRowsAffected(self, query, *args):
		"""ExecuteQueryRowsAffected(str query, []str data) long, str"""
		data = Slice_interface_(args)
		return _etlx.db_DuckDB_ExecuteQueryRowsAffected(self.handle, query, data.handle)
	def ExecuteNamedQuery(self, query, data):
		"""ExecuteNamedQuery(str query, object data) int, str"""
		return _etlx.db_DuckDB_ExecuteNamedQuery(self.handle, query, data.handle)
	def ExecuteQueryPGInsertWithLastInsertId(self, query, *args):
		"""ExecuteQueryPGInsertWithLastInsertId(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_DuckDB_ExecuteQueryPGInsertWithLastInsertId(self.handle, query, data.handle)
	def GetDriverName(self):
		"""GetDriverName() str"""
		return _etlx.db_DuckDB_GetDriverName(self.handle)
	def Query2CSV(self, query, csv_path, *args):
		"""Query2CSV(str query, str csv_path, []str params) bool, str"""
		params = Slice_interface_(args)
		return _etlx.db_DuckDB_Query2CSV(self.handle, query, csv_path, params.handle)
	def IsEmpty(self, value):
		"""IsEmpty(str value) bool"""
		return _etlx.db_DuckDB_IsEmpty(self.handle, value)

# Python type for struct etlxlib.ETLX
class ETLX(go.GoClass):
	"""Expose the library functions\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.etlxlib_ETLX_CTor()
			_etlx.IncRef(self.handle)
			if  0 < len(args):
				self.Config = args[0]
			if "Config" in kwargs:
				self.Config = kwargs["Config"]
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'etlxlib.ETLX{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'etlxlib.ETLX ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Config(self):
		return Map_string_any(handle=_etlx.etlxlib_ETLX_Config_Get(self.handle))
	@Config.setter
	def Config(self, value):
		if isinstance(value, go.GoClass):
			_etlx.etlxlib_ETLX_Config_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	def ExecuteQueryWithRowsAffected(self, conn, sqlData, item, fname, step, dateRef):
		"""ExecuteQueryWithRowsAffected(object conn, object sqlData, object item, str fname, str step, []object dateRef) long, str"""
		return _etlx.etlxlib_ETLX_ExecuteQueryWithRowsAffected(self.handle, conn.handle, sqlData.handle, item.handle, fname, step, dateRef.handle)
	def RunDATA_QUALITY(self, dateRef, conf, extraConf, *args):
		"""RunDATA_QUALITY([]object dateRef, object conf, object extraConf, []str keys) []object, str"""
		keys = go.Slice_string(args)
		return Slice_Map_string_any(handle=_etlx.etlxlib_ETLX_RunDATA_QUALITY(self.handle, dateRef.handle, conf.handle, extraConf.handle, keys.handle))
	def ConfigFromFile(self, filePath):
		"""ConfigFromFile(str filePath) str"""
		return _etlx.etlxlib_ETLX_ConfigFromFile(self.handle, filePath)
	def ConfigFromIpynbJSON(self, ipynbJSON):
		"""ConfigFromIpynbJSON(str ipynbJSON) str"""
		return _etlx.etlxlib_ETLX_ConfigFromIpynbJSON(self.handle, ipynbJSON)
	def ConfigFromMDText(self, mdText):
		"""ConfigFromMDText(str mdText) str"""
		return _etlx.etlxlib_ETLX_ConfigFromMDText(self.handle, mdText)
	def ParseMarkdownToConfig_(self, reader):
		"""ParseMarkdownToConfig_(object reader) str"""
		return _etlx.etlxlib_ETLX_ParseMarkdownToConfig_(self.handle, reader.handle)
	def TracebackHeaders(self, node, source):
		"""TracebackHeaders(object node, []int source) []str"""
		return go.Slice_string(handle=_etlx.etlxlib_ETLX_TracebackHeaders(self.handle, node.handle, source.handle))
	def ParseMarkdownToConfig(self, reader):
		"""ParseMarkdownToConfig(object reader) str"""
		return _etlx.etlxlib_ETLX_ParseMarkdownToConfig(self.handle, reader.handle)
	def PrintConfigAsJSON(self, config, goRun=False):
		"""PrintConfigAsJSON(object config) """
		_etlx.etlxlib_ETLX_PrintConfigAsJSON(self.handle, config.handle, goRun)
	def Walk(self, data, path, fn, goRun=False):
		"""Walk(object data, str path, callable fn) """
		_etlx.etlxlib_ETLX_Walk(self.handle, data.handle, path, fn, goRun)
	def GetRefFromString(self, file):
		"""GetRefFromString(str file) object"""
		return go.time_Time(handle=_etlx.etlxlib_ETLX_GetRefFromString(self.handle, file))
	def ReplaceFileTablePlaceholder(self, key, sql, file_table):
		"""ReplaceFileTablePlaceholder(str key, str sql, str file_table) str"""
		return _etlx.etlxlib_ETLX_ReplaceFileTablePlaceholder(self.handle, key, sql, file_table)
	def GetGODateFormat(self, format):
		"""GetGODateFormat(str format) str"""
		return _etlx.etlxlib_ETLX_GetGODateFormat(self.handle, format)
	def ReplaceQueryStringDate(self, query, dateRef):
		"""ReplaceQueryStringDate(str query, str dateRef) str"""
		return _etlx.etlxlib_ETLX_ReplaceQueryStringDate(self.handle, query, dateRef)
	def ReplaceEnvVariable(self, input):
		"""ReplaceEnvVariable(str input) str"""
		return _etlx.etlxlib_ETLX_ReplaceEnvVariable(self.handle, input)
	def TempFIle(self, content, name):
		"""TempFIle(str content, str name) str, str"""
		return _etlx.etlxlib_ETLX_TempFIle(self.handle, content, name)
	def ConvertIPYNBToMarkdown(self, ipynbContent):
		"""ConvertIPYNBToMarkdown([]int ipynbContent) str, str"""
		return _etlx.etlxlib_ETLX_ConvertIPYNBToMarkdown(self.handle, ipynbContent.handle)
	def LoadREQUIRES(self, conf, *args):
		"""LoadREQUIRES(object conf, []str keys) []object, str"""
		keys = go.Slice_string(args)
		return Slice_Map_string_any(handle=_etlx.etlxlib_ETLX_LoadREQUIRES(self.handle, conf.handle, keys.handle))
	def GetDB(self, conn):
		"""GetDB(str conn) object, str"""
		return go.db_DBInterface(handle=_etlx.etlxlib_ETLX_GetDB(self.handle, conn))
	def SetQueryPlaceholders(self, query, table, path, dateRef):
		"""SetQueryPlaceholders(str query, str table, str path, []object dateRef) str"""
		return _etlx.etlxlib_ETLX_SetQueryPlaceholders(self.handle, query, table, path, dateRef.handle)
	def ReplacePlaceholders(self, sql, item):
		"""ReplacePlaceholders(str sql, object item) str, str"""
		return _etlx.etlxlib_ETLX_ReplacePlaceholders(self.handle, sql, item.handle)
	def ExecuteQuery(self, conn, sqlData, item, fname, step, dateRef):
		"""ExecuteQuery(object conn, object sqlData, object item, str fname, str step, []object dateRef) str"""
		return _etlx.etlxlib_ETLX_ExecuteQuery(self.handle, conn.handle, sqlData.handle, item.handle, fname, step, dateRef.handle)
	def RunETL(self, dateRef, conf, extraConf, *args):
		"""RunETL([]object dateRef, object conf, object extraConf, []str keys) []object, str"""
		keys = go.Slice_string(args)
		return Slice_Map_string_any(handle=_etlx.etlxlib_ETLX_RunETL(self.handle, dateRef.handle, conf.handle, extraConf.handle, keys.handle))
	def RunEXPORTS(self, dateRef, conf, extraConf, *args):
		"""RunEXPORTS([]object dateRef, object conf, object extraConf, []str keys) []object, str"""
		keys = go.Slice_string(args)
		return Slice_Map_string_any(handle=_etlx.etlxlib_ETLX_RunEXPORTS(self.handle, dateRef.handle, conf.handle, extraConf.handle, keys.handle))
	def RunMULTI_QUERIES(self, dateRef, conf, extraConf, *args):
		"""RunMULTI_QUERIES([]object dateRef, object conf, object extraConf, []str keys) []object, str"""
		keys = go.Slice_string(args)
		return Slice_Map_string_any(handle=_etlx.etlxlib_ETLX_RunMULTI_QUERIES(self.handle, dateRef.handle, conf.handle, extraConf.handle, keys.handle))

# Python type for struct db.ODBC
class ODBC(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_etlx.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_etlx.IncRef(self.handle)
		else:
			self.handle = _etlx.db_ODBC_CTor()
			_etlx.IncRef(self.handle)
	def __del__(self):
		_etlx.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'db.ODBC{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'db.ODBC ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def ExecuteQuery(self, query, *args):
		"""ExecuteQuery(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_ODBC_ExecuteQuery(self.handle, query, data.handle)
	def ExecuteQueryRowsAffected(self, query, *args):
		"""ExecuteQueryRowsAffected(str query, []str data) long, str"""
		data = Slice_interface_(args)
		return _etlx.db_ODBC_ExecuteQueryRowsAffected(self.handle, query, data.handle)
	def ExecuteNamedQuery(self, query, data):
		"""ExecuteNamedQuery(str query, object data) int, str"""
		return _etlx.db_ODBC_ExecuteNamedQuery(self.handle, query, data.handle)
	def ExecuteQueryPGInsertWithLastInsertId(self, query, *args):
		"""ExecuteQueryPGInsertWithLastInsertId(str query, []str data) int, str"""
		data = Slice_interface_(args)
		return _etlx.db_ODBC_ExecuteQueryPGInsertWithLastInsertId(self.handle, query, data.handle)
	def Query2CSV(self, query, csv_path, *args):
		"""Query2CSV(str query, str csv_path, []str params) bool, str"""
		params = Slice_interface_(args)
		return _etlx.db_ODBC_Query2CSV(self.handle, query, csv_path, params.handle)
	def GetDriverName(self):
		"""GetDriverName() str"""
		return _etlx.db_ODBC_GetDriverName(self.handle)
	def IsEmpty(self, value):
		"""IsEmpty(str value) bool"""
		return _etlx.db_ODBC_IsEmpty(self.handle, value)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def LoadDotEnv(goRun=False):
	"""LoadDotEnv() """
	_etlx.etlx_LoadDotEnv(goRun)


