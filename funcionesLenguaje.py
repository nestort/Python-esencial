# Variables
tupleA=(1,242,2,43)
varA=2

# str()
# conversión de objeto a cadena.
print(str(1)+str(1))
# _> out: 
# 11
# El resultado es 11 por que los unos se
# volvieron cadena y terminaron '1'+'1'='11'(cocatenados)

# type()
# Obtener el tipo de variable
print(type(varA)) 
# _> out: 
# <class 'int'>
# En este ejemplo el tipo de dato es 'int'

# dir()
# Metodos y/o funciones disponibles 
print("Metodos y/o funciones disponibles:\n",dir(tupleA))
# _> out:
# Metodos y/o funciones disponibles:
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
# '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'count', 'index']

# help()
# Obtener información del objeto.
# ejemplo:
# help(tupleA)
# _> out:
# Built-in subclasses:
#  |      asyncgen_hooks
#  |      UnraisableHookArgs
#  |  
#  |  Methods defined here:
#  |  
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |  
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(self, key, /)
#  |      Return self[key].
#  |  
#  |  __getnewargs__(self, /)
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __hash__(self, /)
#  |      Return hash(self).
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |  
#  |  count(self, value, /)
#  |      Return number of occurrences of value.
#  |  
#  |  index(self, value, start=0, stop=9223372036854775807, /)
#  |      Return first index of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
