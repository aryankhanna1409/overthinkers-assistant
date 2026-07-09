from graphviz import Digraph

def build_flowchart(decision_text, data):
    dot = Digraph(comment="Overthinker's Decision Tree", format='png')
    
    dot.node("D", f" {decision_text}")

    for idx, item in enumerate(data):
        opt_node = f"O{idx}"
        dot.node(opt_node, f"{item['option']}")
        dot.edge("D", opt_node)

        for i, pro in enumerate(item['pros'][:3]):
            pid = f"{opt_node}_P{i}"
            dot.node(pid, f"{pro}", color="green")
            dot.edge(opt_node, pid)

        for i, con in enumerate(item['cons'][:3]):
            cid = f"{opt_node}_C{i}"
            dot.node(cid, f"{con}", color="red")
            dot.edge(opt_node, cid)

    filepath = "static/decision_tree"
    dot.render(filepath, cleanup=True)
    return filepath + ".png"
