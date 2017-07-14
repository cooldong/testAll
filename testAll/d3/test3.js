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
        // console.log(d);
        return d.data.name;
      });
});
// d3.csv("flare.csv",function(error,data){
//   var root = stratify(data)
//         .sort(function(a, b) { return (a.height - b.height) || a.id.localeCompare(b.id); });
//   console.log(root);
// })

var svg = d3.select("#re2").append("svg").attr("width",width).attr("height",height)
var projection = d3.geoMercator()
    .center([107, 31])
    .scale(850)
    .translate([width/2, height/2+150]);
var path = d3.geoPath()
    .projection(projection);
var color = d3.scaleOrdinal(d3.schemeCategory20);
d3.json("china.json", function(error, root) {

    if (error)
        return console.error(error);
    console.log(root.features);

    svg.selectAll("path")
        .data(root.features)
        .enter()
        .append("path")
        .attr("stroke","#000")
        .attr("stroke-width",1)
        .attr("fill", function(d,i){
            return color(i);
        })
        .attr("d", path )   //使用地理路径生成器
        .on("mouseover",function(d,i){
                    d3.select(this)
                       .attr("fill","yellow");
                })
                .on("mouseout",function(d,i){
                    d3.select(this)
                       .attr("fill",color(i));
                });
});
