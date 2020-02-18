const svg = d3.select('svg');
const width = +svg.attr('width');
const height = +svg.attr('height');
const yScale = [];
const xScale = [];

const render = data =>{
    let yValue  = d => d.WeightP;
    const xValue = d => d.Block;
    const margin = {left:300,top:10 ,right:40,bottom:30};
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const yScale = d3.scaleLinear()
        .domain([d3.max(data,yValue),0])
        .range([0,innerHeight]);
    
    const xScale = d3.scaleBand()
        .domain(data.map(xValue))
        .range([0,innerWidth])
        .padding(0.1);
    
    const g = svg.append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);

    var myColor = d3.scaleSequential().domain([d3.min(data,yValue),d3.max(data,yValue)])
    .interpolator(d3.interpolateRdYlGn);
      //tooltip
// Define the div for the tooltip
const onMouseOver = d =>{	
            div.transition().duration(200).style("opacity", .9);		
            div	.html(xValue(d)+"<br>"+yValue(d))
              	.style("left", d3.event.pageX + "px")
              	.style("top",  d3.event.pageY - 30 + "px");	
            }
var div = d3.select("body").append("div")	
    .attr("class", "tooltip")				
    .style("opacity", 1);
  
       var bars =   g.selectAll("rect").data(data)
        .enter().append('rect')
            .attr('x', d => xScale(d.Block))
            .attr('y', d => yScale(yValue(d)))
            .attr('height',d => innerHeight - yScale(yValue(d)))
            .attr('width',xScale.bandwidth())
            .attr("fill", d => myColor(yValue(d)))
       			.on("mouseover", d => onMouseOver(d))					
        		.on("mouseout", function(d) {		
            div.transition()		
                .duration(500)		
                .style("opacity", 0);	
        });
       
       //update new values
       var mytext = g.selectAll("text").data(data)
            .enter().append("text")
            .text(d => yValue(d))
            .attr('x', d => xScale(d.Block)+25)
            .attr('y', d => yScale(yValue(d))+15)
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")

    var yaxis = g.append('g')
        .call(d3.axisLeft(yScale));
    
    g.append('g').call(d3.axisBottom(xScale))
        .attr('transform',`translate(0, ${innerHeight})`);
  
       makeviz = opt =>{
         let tansitionDuration = 1000;
      		if(opt == 1){
            yValue  = d => d.HeightP;
            console.log('height');
          }else if (opt == 2 ){
          	yValue  = d => d.WeightP;
            console.log('weight');
          }else{
          	yValue  = d => d.HeightWeightP;
          }
      const yScale = d3.scaleLinear()
        .domain([d3.max(data,yValue),0])
        .range([0,innerHeight]);
       		
        bars.transition().duration(tansitionDuration)
      			.attr('y', d => yScale(yValue(d)))
            .attr('height',d => innerHeight - yScale(yValue(d)))
            .attr("fill", d => myColor(yValue(d)))


        // Remove old ones
        bars.exit().remove();
         
         
         //text update
         mytext.transition().duration(tansitionDuration)
          .text(d => yValue(d))
            .attr('y', d => yScale(yValue(d))+15);
         
         mytext.exit().remove();
         
         // y axis update
         
         yaxis.transition().duration(tansitionDuration)
        .call(d3.axisLeft(yScale));
         
       }   
    
      
    

const dropdownChange = () =>{
	var sel = document.getElementById('opt');
  val = document.getElementById("opt").value
  makeviz(val);
}
makeviz(1);

const dropdownList = ['Height','Weight'];
var dropdown = d3.select("#opt")
    .on("change", dropdownChange);
}


const monthwise = (data) => {
data.forEach(d => {
        d.HeightP = +d.HeightP;
        d.WeightP = +d.WeightP;
        d.HeightWeightP = +d.HeightWeightP;
    });
    var aproperty = [];
    var sproperty = [];
    var oproperty = [];
  data.forEach(d =>{
    var temp = {};
		temp['Block'] = d.Block;
		temp['HeightP'] = d.HeightP;
		temp['WeightP'] = d.WeightP;
		temp['HeightWeightP'] = d.HeightWeightP;
    if(d.Month == "Aug"){
			aproperty.push(temp);
    }else if (d.Month == "Sep"){
    	sproperty.push(temp);
    }else if (d.Month == "Oct"){
    	oproperty.push(temp);
    }
    
  })

var listdata = [
  aproperty,sproperty,oproperty
]
return listdata;
}

const selectData =  (val,monthwiseData) =>{
if(val == "aug"){
    	return monthwiseData[0];
  }else if (val == "sep"){
  		return monthwiseData[1];
  }else if (val == 'oct'){
    	return monthwiseData[2]       
    }
}
const sortData = (data,parameter) =>{

}
d3.csv("{% url 'play_count_by_month' %}").then(data => {
  	monthwiseData = monthwise(data);
		d3.select("#monthdropdown")
    .on("change", () =>{
  				val = document.getElementById("monthdropdown").value
  				mydata = selectData(val,monthwiseData);
      		console.log(mydata);
					svg.selectAll("*").remove();
      		render(mydata);
    	});
		augData = monthwiseData[0];
  	console.log(augData);
    render(augData); 
})

