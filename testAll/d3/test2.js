var svgWidth = 400
var svgHeight = 400
var svg1 = d3.select("#re1").append("svg").attr("width",svgWidth).attr("height",svgHeight)
var dataset = [ 30 , 10 , 43 , 55 , 13 ];
var color = d3.scaleOrdinal(d3.schemeCategory10);
var pie = d3.pie()
var piedata = pie(dataset)
var arc = d3.arc()
              .innerRadius(0)
              .outerRadius(150)
var arcs = svg1.selectAll("g")
                .data(piedata)
                .enter()
                .append("g")
                .attr("transform","translate("+svgWidth/2+","+svgHeight/2+")")
arcs.append("path")
    .attr("fill",function(i){
      return color(i.index)
    })
    .attr("d",function(d){
      return arc(d)
    })
arcs.append("text")
    .attr("transform",function(d){
      return "translate("+arc.centroid(d)+")"
    })
    .attr("text-anchor","middle")
    .text(function(d){
        return d.data;
    });

var svg2 = d3.select("#re2").append("svg").attr("width",svgWidth).attr("height",svgHeight);
var nodes = [ { name: "桂林" }, { name: "广州" },
              { name: "厦门" }, { name: "杭州" },
              { name: "上海" }, { name: "青岛" },
              { name: "天津" } ];

var edges = [ { source : 0 , target: 1 } , { source : 0 , target: 2 } ,
               { source : 0 , target: 3 } , { source : 1 , target: 4 } ,
               { source : 1 , target: 5 } , { source : 1 , target: 6 } ];
var force = d3.forceSimulation(nodes)
              .force("link",d3.forceLink(edges).distance(150))
              .force("charge",d3.forceManyBody().strength(-400))
              .force("center", d3.forceCenter(svgWidth/2,svgHeight/2))
force.on("tick", function(){ //对于每一个时间间隔
    //更新连线坐标
    svg_edges.attr("x1",function(d){ return d.source.x; })
        .attr("y1",function(d){ return d.source.y; })
        .attr("x2",function(d){ return d.target.x; })
        .attr("y2",function(d){ return d.target.y; });

    //更新节点坐标
    svg_nodes.attr("cx",function(d){ return d.x; })
        .attr("cy",function(d){ return d.y; });

    //更新文字坐标
    // svg_texts.attr("x", function(d){ return d.x; })
    //    .attr("y", function(d){ return d.y; });
 });
force.force("link").links(edges)
var svg_edges = svg2.selectAll("line")
                    .data(edges)
                    .enter()
                    .append("line")
                    .style("stroke","#ccc")
                    .style("stroke-width",1)
var color2 = d3.scaleOrdinal(d3.schemeCategory20);
var svg_nodes = svg2.selectAll("circle")
                    .data(nodes)
                    .enter()
                    .append("circle")
                    .attr("r",20)
                    .style("fill",function(i,d){
                      return color2(i)
                    })
                    .call(d3.drag().on("start", dragstarted)
                                    .on("drag", dragged)
                                    .on("end", dragended))
function dragstarted(d) {
  if (!d3.event.active) force.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) force.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
svg_nodes.append("title").text(function(d){
  return d.name;
})
// var svg_texts = svg2.selectAll("text")
//                     .data(nodes)
//                     .enter()
//                     .append("text")
//                     .style("fill","black")
//                     .attr("dx",20)
//                     .attr("dy",8)
//                     .text(function(i,d){
//                       return d.name;
//                     })
