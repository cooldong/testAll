var svgWidth = 400
var svgHeight = 400
var svg1 = d3.select("#re1").append("svg").attr("width",svgWidth).attr("height",svgHeight)
var dataset = [ 30 , 10 , 43 , 55 , 13 ];
var color = d3.scale.category10();
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
      return color(i)
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
