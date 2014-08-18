/* [ ---- Gebo Admin Panel - datatables ---- ] */

	$(document).ready(function() {
		// horizontal scroll
		gebo_datatbles.dt_b();
	});
	
	//* calendar
	gebo_datatbles = {
        dt_b: function() {
			$('#dt_b').dataTable({
				//"sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
                "sScrollX": "100%",
                "sScrollXInner": '110%',
                "sPaginationType": "bootstrap",
                "bScrollCollapse": true 
				//"bJQueryUI":true
				//"iDisplayLength":6
            });
		},
	};