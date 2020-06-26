class Tree(object):
	def __init__(self,l,r):
		self.l = l
		self.r = r
		self.v = 0
		self.left = None # 初始化节点值
		self.right = None
		if l < r:        # 构造规则，区分左右节点
			mid = (l + r)/2 
			self.left = Tree(l,mid)
			self.right = Tree(mid+1,r) 
	
	def push_up(self): # 更新规则
	self.v = self.left.v + self.right.v

	def set_v(self,p,v): # 单点更新，p为需要更新的节点编号，v为更新值
		if self.l == self.r: # 当l==r时，即为找到相应节点
			self.v = v
			return
		mid = (self.l + self.r)/2
		if p <= mid:
			self.left.set_v(p,v)
		else:
			self.right.set_v(p,v)
		self.push_up() # 调用更新规则
	
	def query(self,x,y): # 区间查询
		if x <= self.l and y>=self.r:
			return self.v
		if self.l == self.r:
			return self.v
		mid = (self.l + self.r)/2
		if mid >= y:
			return self.left.query(x,y)
		elif mid < x:
			return self.right.query(x,y)
		else:
			return self.left.query(x,mid) + self.right.query(mid+1,y)
