import torch

class ReLU:

	def __init__():
		self.output = None
		self.gradInput = None
	
	def forward(self, inp):
		# if input = n x d
		self.output = inp # torch.max(inp, torch.zeros(inp.size()).double())
		self.output[< 0 ] = 0
		return self.output

	def backward(self, inp, gradOutput):
		DomByDon = self.output
		DomByDon[> 0] = 1
		self.gradInput = gradOutput * DomByDon
		return self.gradInput