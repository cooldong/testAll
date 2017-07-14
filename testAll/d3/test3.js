var width = 800;
var height = 600;
var g = d3.select("#re1").append("svg").attr("width",width).attr("height",height).attr("transform","translate("+50+","+0+")")
var tree = d3.tree()
    .size([height, width - 160]);

// var stratify = d3.stratify()
//     .parentId(function(d) { return d.id.substring(0, d.id.lastIndexOf(".")); });

d3.json("city_tree.json", function(error, data) {
  if (error) throw error;

  var root = d3.hierarchy(data);

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
      .text(function(d) {
        console.log(d);
        return d.data.name;
      });
});
// d3.csv("flare.csv",function(error,data){
//   var root = stratify(data)
//         .sort(function(a, b) { return (a.height - b.height) || a.id.localeCompare(b.id); });
//   console.log(root);
// })
