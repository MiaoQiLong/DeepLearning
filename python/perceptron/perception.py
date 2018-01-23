class Perceptron(object):
	def __init__(self,input_num,activator):
		self.activator=activator
		self.weights=[0.0 for _ in range(input_num)]
		self.bias=0.0

	def __str__(self):
		return 'weights\t:%s\nbias\t:%f\n' % (self.weights,self.bias)

	def predict(self,input_vec):
		return self.activator(
			reduce(lambda a,b:a+b,
				map(lambda (x,w):x*w,zip(input_vec,self.weights)),
				0.0+self.bias)

	def train(self,input_vec,labels,iteration,rate):
		samples=zip(input_vec,labels)
		for(input_vec,label) in samples
			output=self.predict(input_vec)
			self._updata_weights(input_vec,output,label,rate)


	def _updata_weights(self,input_vec,output,label,rate)
		delta=label-output
		self.weights=map(lambda (x,w):w+rate*deta*x,
				zip(input_vec,self,weights))
		self.bias+=rate*delta
