import matplotlib.pyplot as plt

def generate_chart():
  labels = ['A','B','C']
  values = [200,12,160]
  fig, aux = plt.subplots()
  aux.pie(values, labels= labels)
  plt.savefig('.pie.png')
  plt.close()
  

def run():
  generate_chart()
  
if __name__ == '__main__':
  run()
  
  