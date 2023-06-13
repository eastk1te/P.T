from torch.optim.lr_scheduler import ConstantLR, _LRScheduler, SequentialLR
from torch.optim.optimizer import Optimizer
import warnings

def decay_after_k_epoch(optim: Optimizer, n_epochs:int, init_lr: float, target_lr: float, decay_after:int=100):

    scheduler1 = ConstantLR(optim, factor=1, total_iters=decay_after)
    scheduler2 = LinearDecayLR(optim, initial_lr = init_lr, target_lr=target_lr, total_iters=n_epochs-decay_after) # constant는 그냥 한 번 줄여주고 마는 거임.

    scheduler = SequentialLR(optim, schedulers=[scheduler1, scheduler2], milestones=[decay_after])
    return scheduler


class LinearDecayLR(_LRScheduler):

    def __init__(self, optimizer:Optimizer, initial_lr: float, target_lr:float, total_iters:int, last_epoch:int=-1, verbose:bool=False):
        
        if initial_lr < 0:
            raise ValueError("Initial Learning rate expected to be a non-negative integer.")
            
        if target_lr < 0:
            raise ValueError("Target Learning rate expected to be a non-negative integer.")

        if target_lr > initial_lr:
            raise ValueError("Target Learning Rate must be larger than Initial Learning Rate.")

        self.init_lr = initial_lr
        self.target_lr = target_lr
        self.total_iters = total_iters
        self.subtract_lr = self._get_decay_constant()
        
        super(LinearDecayLR, self).__init__(optimizer, last_epoch, verbose) 
        
    def _get_decay_constant(self):
        return float((self.init_lr-self.target_lr)/self.total_iters)
        
    def get_lr(self):
        if not self._get_lr_called_within_step:
            warnings.warn("To get the learning rate computed by the scheduler, "
                        "please use 'get_last_lr()'.", UserWarning)

        return [group['lr']-self.subtract_lr for group in self.optimizer.param_groups]


class DelayedLinearDecayLR(LinearDecayLR):
    def __init__(self, optimizer:Optimizer, initial_lr: float, target_lr: float, total_iters:int, last_epoch:int=-1, decay_after:int=100, verbose:bool=False):
        self.decay_after = decay_after
        
        super(DelayedLinearDecayLR, self).__init__(optimizer, initial_lr, target_lr, total_iters, last_epoch, verbose)

    
    def get_lr(self):
        if not self._get_lr_called_within_step:
            warnings.warn("To get the learning rate computed by the scheduler, "
                        "please use 'get_last_lr()'.", UserWarning)

        if self.decay_after <= self.last_epoch < (self.decay_after + self.total_iters): 
            return [group['lr']-self.subtract_lr for group in self.optimizer.param_groups]

        else:
            return [group['lr'] for group in self.optimizer.param_groups]