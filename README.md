# 基于Python实现线段树

---

## 前言

这两天开始正式学Python，看了些基础教程感觉还不错，于是想着写一些代码练练手。想起来最开始学C++也是敲的数据结构，于是准备基于Python撸一些数据结构，先拿线段树开刀吧！

## 实现目标  
__1. 线段树的定义与构造__  

__2. 线段树的单点更新__  

__2. 线段树的区间查询__



### 线段树的定义与构造


线段树的定义是Python与c++代码风格的主要区别  
先看看我的c++线段树定义：

```c++

struct node
{
    node *l, *r; //当前节点的左右树
    int v;       //节点值
    node(int vv, node *ll, node *rr) { l = ll, r = rr, v = vv; }
};

```

观察可知，主要由两部分构成：
__1. 指向自己的指针，也就是左右结点__
__2. 构造函数__

在Python中，构造函数通过定义class中的 “\__init__” 函数来实现，而左右节点的指针可以通过“\__init__”中的self参数来指向自身的其他参数来实现，代码如下：

```python

class node(object):
	def __init__(self,l,r):
		self.l = l # 当前节点的左右树
		self.r = r 
        self.v = 0 # 节点值

```

现在弄清楚了Python中线段树节点定义与C++的区别，现在就可以将构造节点的代码移植过来了！代码如下：

```python

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

# 在主函数中，可以直接以 Tree(0,N) 构造出n个节点的线段树了！

```

### 线段树的单点更新

线段树的单点更新主要分为两部分：
__1. 用于区间查询的更新规则（求区间和或者区间最值）__
__2. 找到相应节点并进行递归更新__

为了保证低耦合，更新规则可以单独提出来；这里以区间和为例，代码如下：

```python

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

```
### 线段树的区间查询

区间查询实现的是对线段树中指定区间的查询。根据构树规则可以查询区间和，区间最大值等等。代码如下：

```python

def query(self,x,y): # 区间查询
	if x <= self.l and y>=self.r: 
			return self.v
	if self.l == self.r:
		return self.v # 当前的区间真包含于查询的区间内，即为答案
	mid = (self.l + self.r)/2

	if mid >= y: # 左子树与需要查询的区间交集非空
		return self.left.query(x,y)
	elif mid < x: # 右子树和查询的交集非空
		return self.right.query(x,y)
	else: # 没有找到，继续找当前节点的左右子树
		return self.left.query(x,mid) + self.right.query(mid+1,y)

```

