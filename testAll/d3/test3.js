var svgWidth = 400;
var svgHeight = 400;
var g = d3.select("#re1").append("svg").attr("width",svgWidth).attr("height",svgHeight)
var tree = d3.tree()
tree.size([svgWidth, svgHeight-200])
tree.separation(function(a, b) { return (a.parent == b.parent ? 1 : 2); });
d3.json("city_tree.json", function(error, root) {
  console.log(tree(root));
  var link = g.selectAll(".link")
      .data(tree(root).links())
      .enter().append("path")
        .attr("class", "link")
        .attr("d", d3.linkHorizontal()
            .x(function(d) { return d.y; })
            .y(function(d) { return d.x; }));

    var node = g.selectAll(".node")
      .data(root.descendants())
      .enter().append("g")
        .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
        .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })

    node.append("circle")
        .attr("r", 2.5);

    node.append("text")
        .attr("dy", 3)
        .attr("x", function(d) { return d.children ? -8 : 8; })
        .style("text-anchor", function(d) { return d.children ? "end" : "start"; })
        .text(function(d) { return d.id.substring(d.id.lastIndexOf(".") + 1); });
})
