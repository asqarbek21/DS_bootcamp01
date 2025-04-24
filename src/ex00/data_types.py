def data_types():
      """prints data types"""
      a = 1
      b = "word"
      c = 1.3
      d = True
      e = [1, 2, 3, 4, 5]
      f = {"brand":"audi"}
      g = (1, 2, 3, 4, 5)
      h = {"audi", "bmw", "mercedes"}
      
      types  = [type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h)]
      type_names = [t.__name__ for t in types]
      print(f"[{', '.join(type_names)}]")

if __name__ == '__main__':
      data_types()
