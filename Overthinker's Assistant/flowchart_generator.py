import textwrap

from graphviz import Digraph


def _wrap(text, width=34):
    """Wrap long sentences so nodes stay narrow and the tree stays readable."""
    return "\n".join(textwrap.wrap(str(text), width)) or " "


def build_flowchart(decision_text, data):
    dot = Digraph(comment="Overthinker's Decision Tree", format='png')

    # Left-to-right layout keeps the image compact instead of thousands of pixels wide.
    dot.attr(rankdir="LR", bgcolor="white", nodesep="0.25", ranksep="0.6", dpi="130")
    dot.attr("node", shape="box", style="rounded,filled", fontname="Helvetica",
             fontsize="11", fillcolor="#f8f9fa", color="#adb5bd", margin="0.15,0.08")
    dot.attr("edge", color="#adb5bd", arrowsize="0.7")

    dot.node("D", _wrap(decision_text, 24), fillcolor="#212529", fontcolor="white",
             color="#212529", fontsize="13")

    for idx, item in enumerate(data):
        opt_node = f"O{idx}"
        dot.node(opt_node, _wrap(item['option'], 22), fillcolor="#cfe2ff", color="#0d6efd",
                 fontsize="12")
        dot.edge("D", opt_node)

        for i, pro in enumerate(item['pros'][:3]):
            pid = f"{opt_node}_P{i}"
            dot.node(pid, _wrap(pro), fillcolor="#d1e7dd", color="#198754")
            dot.edge(opt_node, pid, color="#198754")

        for i, con in enumerate(item['cons'][:3]):
            cid = f"{opt_node}_C{i}"
            dot.node(cid, _wrap(con), fillcolor="#f8d7da", color="#dc3545")
            dot.edge(opt_node, cid, color="#dc3545")

    filepath = "static/decision_tree"
    dot.render(filepath, cleanup=True)
    return filepath + ".png"
