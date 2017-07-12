var svgWidth = 400
var svgHeight = 400
var svg = d3.select("#re1").append("svg").attr("width",svgWidth).attr("height",svgHeight)
var circle1 = svg.append("circle").attr("cx",100)
                  .attr("cy",100).attr("r",45).style("fill","green")
var circle2 = svg.append("circle").attr("cx",100)
                  .attr("cy",200).attr("r",45).style("fill","green")
var circle3 = svg.append("circle").attr("cx",100)
                  .attr("cy",300).attr("r",45).style("fill","green")
circle1.transition().duration(1000).ease(d3.easeCircle).attr("cx",300).style("fill","red").attr("r",25)
circle2.transition().duration(1000).ease(d3.easeElastic).attr("cx",300).style("fill","red").attr("r",25)
circle3.transition().duration(1000).ease(d3.easeBounce).attr("cx",300).style("fill","red").attr("r",25)

var padding = {left:30, right:30, top:20, bottom:20};
var svgrect = d3.select("#re2").append("svg").attr("width",svgWidth).attr("height",svgHeight)
var dataset = [10, 20, 30, 40, 33, 24, 12, 5];
var xscale = d3.scaleBand()
              .domain(d3.range(dataset.length))
              .rangeRound([0,svgWidth-padding.left-padding.right])
var yscale = d3.scaleLinear()
              .domain([0,d3.max(dataset)])
              .range([svgHeight-padding.top-padding.bottom,0])
var xaxis = d3.axisBottom(xscale)
var yaxis = d3.axisLeft(yscale)
var rectPadding = 4;
var rect = svgrect.selectAll(".MyRect")
                  .data(dataset).enter()
                  .append("rect")
                  .attr("class","MyRect")
                  .attr("transform","translate("+padding.left+","+padding.top+")")
                  .attr("x",function(d,i){
                    return xscale(i)+rectPadding/2
                  })
                  .attr("y",function(d,i){
                    var min = yscale.domain()[0]
                    return yscale(min)
                    // return yscale(d)
                  })
                  .attr("width",xscale.bandwidth()-rectPadding)
                  .attr("height",function(d){
                    return 0
                    // return svgHeight-padding.top-padding.bottom-yscale(d)
                  })
                  .attr("fill","steelblue")
                  .on("mouseover",function(d,i){
                    d3.select(this).attr("fill","yellow")
                  })
                  .on("mouseout",function(d,i){
                    d3.select(this)
                      // .transition()
                      // .duration(200)
                      // .ease(d3.easeBounce)
                      .attr("fill","steelblue")
                  })
                  .transition()
                  .delay(function(i){
                    return 50*i
                  })
                  .duration(500)
                  .ease(d3.easeBounce)
                  .attr("height",function(d){
                    return svgHeight-padding.top-padding.bottom-yscale(d)
                  })
                  .attr("y",function(d){
                    return yscale(d)
                  })

var texts = svgrect.selectAll(".MyText")
                    .data(dataset).enter()
                    .append("text")
                    .attr("class","MyText")
                    .attr("transform","translate("+padding.left+","+padding.top+")")
                    .attr("x",function(d,i){
                      return xscale(i)+rectPadding/2
                    })
                    .attr("y",function(d){
                      var min = yscale.domain()[0]
                      return yscale(min)
                      // return yscale(d)
                    })
                    .attr("dx",(xscale.bandwidth()-rectPadding)/2)
                    .attr("dy",function(d){
                      return 20
                    })
                    .text(function(d){
                      return d
                    })
                    .transition()
                    .delay(function(i){
                      return 50*i
                    })
                    .duration(500)
                    .ease(d3.easeBounce)
                    .attr("y",function(d){
                      return yscale(d)
                    })
svgrect.append("g")
        .attr("class","axis")
        .attr("transform","translate("+padding.left+","+(svgHeight-padding.bottom)+")")
        .call(xaxis)
svgrect.append("g")
        .attr("class","axis")
        .attr("transform","translate("+padding.left+","+padding.top+")")
        .call(yaxis)
// svgrect.on("click",function(){
//   console.log(d3.event);
// })
