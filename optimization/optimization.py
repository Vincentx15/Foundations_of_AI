import torch
n_iter = 10000
a = torch.tensor(3.0, requires_grad=True)
x = 1
y = 2
opt = torch.optim.SGD([a], lr=0.01, momentum=0.01)

for i in range(n_iter):
    loss = (y - a * x) ** 2
    loss.backward()
    opt.step()
    opt.zero_grad()
    print(i, a.item(), loss.item())
