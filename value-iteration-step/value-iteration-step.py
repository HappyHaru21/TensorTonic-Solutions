def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here
    num_states = len(values)
    new_values = []
    for s in range(num_states):
        max_q_val = float('-inf')
        num_actions = len(rewards[s])
        for a in range(num_actions):
            expected_val = 0
            for s_prime in range(num_states):
                probability = transitions[s][a][s_prime]
                value_prime = values[s_prime]
                expected_val+= probability*value_prime
            q_val = rewards[s][a] + (gamma*expected_val)
            if q_val>max_q_val:
                max_q_val=q_val
        new_values.append(max_q_val)
    return new_values