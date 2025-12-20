class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda r: r.record_id)

    nodes = {}

    for index, record in enumerate(records):
        rid = record.record_id
        pid = record.parent_id

        # IDs must be continuous starting at 0
        if rid != index:
            raise ValueError("Record id is invalid or out of order.")

        # Only root may have parent == itself
        if pid == rid and rid != 0:
            raise ValueError("Only root should have equal record and parent id.")

        # Parent ID must not be greater than record ID
        if pid > rid:
            raise ValueError("Node parent_id should be smaller than its record_id.")

        # Root validation
        if rid == 0:
            if pid != 0:
                raise ValueError("Root node parent_id should be equal to its record_id.")
            nodes[0] = Node(0)
            continue

        # Parent must already exist
        if pid not in nodes:
            raise ValueError("Parent node does not exist.")

        node = Node(rid)
        nodes[rid] = node
        nodes[pid].children.append(node)

    return nodes[0]
