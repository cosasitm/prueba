import matplotlib.pyplot as plt

def generate_chart():
  labels = ['A','B','C']
  values = [200,12,160]
  fig, aux = plt.subplot()
  aux.pie(values, labels= labels)
  plt.savefig('.pie.png')
  plt.close()
  