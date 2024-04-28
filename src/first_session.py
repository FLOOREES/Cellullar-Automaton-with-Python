"""
En aquesta sessió generarem un codi en Python, R o C++ que ens permeti implementar un autòmat cel·lular que segueixi les regles de wolfram,
 definides a:

https://mathworld.wolfram.com/ElementaryCellularAutomaton.html

Podeu i de fet, es recomana, que empreu alguna IA com Copilot o ChatGPT, per agilitzar la generació de codi.

Un cop fet això es generalitzarà l'autòmat per permetre combinar diferents regles en un mateix autòmat, generant una estructura multicapa,
 com la presentada a teoria.

Al final de la sessió hauríem de tenir un autòmat que pogués implementar les regles bàsiques i mostrar l'evolució de forma temporal en un
 gràfic per una regla simple o per una combinació de elles.
"""

import matplotlib.pyplot as plt

def rule_to_bin(rule_number):
    """ Convert the rule number to a binary representation. """
    return f"{rule_number:08b}"

def apply_rule(rule_bin, left, center, right):
    """ Apply the rule to determine the new state of a cell. """
    index = 7 - (left * 4 + center * 2 + right)
    return int(rule_bin[index])

def elementary_ca(rule_number, initial_state, generations):
    """ Generate an elementary cellular automaton. """
    rule_bin = rule_to_bin(rule_number)
    current_state = initial_state
    result = [current_state]
    
    for _ in range(generations - 1):
        new_state = []
        current_state = [0] + current_state + [0]  # Add zero-padding for edge cases
        for i in range(1, len(current_state) - 1):
            new_state.append(apply_rule(rule_bin, current_state[i-1], current_state[i], current_state[i+1]))
        result.append(new_state)
        current_state = new_state
    
    return result

def print_ca(result):
    """ Print the cellular automaton's states. """
    for state in result:
        print("".join('█' if x else ' ' for x in state))

# Example usage:
initial_state = [0]*15 + [1] + [0]*15
generations = 30
rule_number = 2  # You can change this to any rule from 0 to 255

result = elementary_ca(rule_number, initial_state, generations)
#print_ca(result)

def update_layer(rule_bin, layer, upper_layer=None, lower_layer=None):
    """ Update a single layer based on its rule and optionally influenced by adjacent layers. """
    padded_layer = [0] + layer + [0]  # Padding to handle edges
    if upper_layer:
        upper_layer = [0] + upper_layer + [0]
    if lower_layer:
        lower_layer = [0] + lower_layer + [0]
    
    new_layer = []
    for i in range(1, len(padded_layer) - 1):
        center = padded_layer[i]
        left = padded_layer[i-1]
        right = padded_layer[i+1]
        # Influence from upper and lower layers can be added here
        # For simplicity, this example ignores upper and lower influences
        new_cell_state = apply_rule(rule_bin, left, center, right)
        new_layer.append(new_cell_state)
    return new_layer

def multicellular_automaton(rules, initial_states, generations):
    """ Simulate a multicellular automaton with multiple layers. """
    rule_bins = [rule_to_bin(rule) for rule in rules]
    current_states = initial_states
    results = [current_states]
    
    for _ in range(generations - 1):
        new_states = []
        for layer_index, layer in enumerate(current_states):
            rule_bin = rule_bins[layer_index]
            # Get adjacent layers if exist
            upper_layer = current_states[layer_index-1] if layer_index > 0 else None
            lower_layer = current_states[layer_index+1] if layer_index < len(current_states)-1 else None
            new_layer = update_layer(rule_bin, layer, upper_layer, lower_layer)
            new_states.append(new_layer)
        results.append(new_states)
        current_states = new_states
    
    return results

def print_multilayer_ca(results):
    """ Print the states of a multicellular automaton. """
    for generation in results:
        for layer in generation:
            print("".join('█' if x else ' ' for x in layer))
        print("\n--- Next Generation ---\n")

# Example usage
rules = [27, 2, 5]  # Different rules for each layer
initial_states = [[0]*15 + [1] + [0]*15 for _ in range(3)]  # Same initial state for simplicity
generations = 30

result = multicellular_automaton(rules, initial_states, generations)
#print_multilayer_ca(result)

def plot_multilayer_ca(results):
    """ Plot the states of a multicellular automaton using matplotlib. """
    num_layers = len(results[0])
    fig, axes = plt.subplots(num_layers, 1, figsize=(10, num_layers * 2))
    
    if num_layers == 1:
        axes = [axes]  # Make it iterable if there's only one layer
    
    for generation in results:
        for layer_index, layer in enumerate(generation):
            ax = axes[layer_index]
            ax.clear()  # Clear the previous plot for this layer
            ax.imshow([layer], aspect='auto', cmap='binary')
            ax.set_title(f"Layer {layer_index+1} - Generation {results.index(generation)+1}")
            ax.set_yticks([])
            ax.set_xticks([])
        plt.pause(0.5)  # Pause to visually see the update
        
    plt.show()

# Example usage
result = multicellular_automaton(rules, initial_states, generations)
plot_multilayer_ca(result)