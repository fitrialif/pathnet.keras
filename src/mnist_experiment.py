import pickle

import keras.backend as K

from genetic_agents import GeneticAgents
from pathnet import PathNet
from task_manager import TaskManager
from utils import reset_all_weigths

# parameters for genetic agents and path net architecture
num_layers = 3
num_modules_per_layer = 10
num_neurons_per_module = 20
output_size = 2
# parameters for the task manager
class_arg_list = [[4, 5], [6, 7]]
val_accuracy_treshold = .90
dataset_name = 'mnist'
save_path = '../trained_models/'
num_experiments = 200
genetic_epochs = []
for experiment_arg in range(num_experiments):
    print('Experiment:', experiment_arg)
    genetic_agents = GeneticAgents(shape=(num_modules_per_layer, num_layers))
    pathnet = PathNet(shape=(num_modules_per_layer, num_layers),
                num_neurons_per_module=num_neurons_per_module,
                output_size=output_size)
    task_manager = TaskManager(pathnet, genetic_agents,
                            dataset_name, class_arg_list,
                            accuracy_treshold=val_accuracy_treshold)
    reset_all_weigths(save_path)
    task_manager.train_tasks()
    genetic_epochs.append(task_manager.genetic_epochs)
    K.clear_session()
pickle.dump(genetic_epochs, open('mnist_results.p', 'wb'))

