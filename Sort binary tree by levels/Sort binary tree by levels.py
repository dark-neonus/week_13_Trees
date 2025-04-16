def tree_by_levels(node):
    if node is None:
        return []
    queue = [node]
    result = []
    while len(queue) > 0:
        head_queue = queue[0]
        queue.pop(0)
        result.append(head_queue.value)
        if head_queue.left:
            queue.append(head_queue.left)
        if head_queue.right:
            queue.append(head_queue.right)

    return result
