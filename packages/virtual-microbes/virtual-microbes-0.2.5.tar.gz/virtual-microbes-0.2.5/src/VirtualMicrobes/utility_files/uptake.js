/***************************
!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	coalescence
!!!!!!!!!!!!!!!!!!!!!!!!!!!!
***************************/

gs.push( new Dygraph(
document.getElementById("graph_uptake"),
"population_dat/uptake_rates.csv", // path to CSV file
{
title: 'eDNA uptake rates',
xlabel: 'Simulation time',
ylabel: '',
//showRangeSelector: true,
//valueRange: [-0.01,1.01],

legend: 'always',
labelsDiv: document.getElementById('legend_uptake'),

//labelDivWidth: 0,
visibility: [true,true,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false],

colors: ['#3333FF', '#FF3333', '#000000', '#55CC55', '#5555FF', '#FF33FF'],

//rangeSelectorHeight: 30,
// rangeSelectorPlotStrokeColor: 'black',
// rangeSelectorPlotFillColor: 'black',

	// highlightSeriesOpts: {
	//   strokeWidth: 2,
	//   strokeBorderWidth: 1,
	//   highlightCircleSize: 5
	// },
	series: {
			'avrg': {
			strokePattern: null,
			fillGraph: true,
			drawPoints: true,
				pointSize: 1,
			strokeWidth: 0.0,
			},
			'min': {
			strokePattern: null,
			strokeWidth: 1.0,
			},
			'max': {
			strokePattern: null,
			strokeWidth: .0,
				drawPoints:true,

			},
			'median': {
			strokePattern: Dygraph.DOTTED_LINE,
			strokeWidth: 1,
			visibility: false,
			},
			'Avg-std': {
			strokePattern: Dygraph.DOTTED_LINE,
			strokeWidth: 3,
			visibility: false,
			},
			'Maxfitmut': {
			//strokePattern: Dygraph.DOT_DASH_LINE,
			strokePattern: null,
			strokeWidth: 0,
			fillGraph: true,
			drawPoints:true,
			//highlightCircleSize: 3
			}
			},
drawCallback: function(me, initial) {
		if (blockRedraw || initial) return;
		blockRedraw = true;
		var range = me.xAxisRange();
	// var yrange = me.yAxisRange();
		for (var j = 0; j < gs.length; j++) {
		if (gs[j] == me) continue;
		gs[j].updateOptions( {
		dateWindow: range,
		//valueRange: yrange
		} );
		}
		blockRedraw = false;
	},
rollPeriod: 1,
showRoller: true,
animatedZooms: false,
	group: "all",
}          // options
)
)
