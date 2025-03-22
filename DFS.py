def dfs(Node, value):
    node.visited = True


    if node.value == value:
        return node
    
    for negh in node.adjecentlist:
        if not negh.visited:
            negh.visited = True
            dfs(negh,value)