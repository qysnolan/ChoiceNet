$(document).ready(function() {
    if(hash == "deleted") {
        $("#deletedNotice").fadeIn();
    }

    $("#evaluationsTable").dataTable({
        "iDisplayLength": 25,
        "aaSorting": [["1", "desc"]],
        
        "sDom": "<'row-fluid'<'span6'lC><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
        
        "oColVis": {
            "buttonText": "Change Columns",
            "bRestore": true,
            "sRestore": "Show default",
            "aiExclude": [0, 1, 6, 7, 8]
        },
        "bStateSave": true,
        "aoColumnDefs": [
            { "bVisible": false, "aTargets": [0, 4] },
            { "iDataSort": 0, "aTargets": [1] },
            { "bSearchable": false, "sClass": "cell-center", "aTargets": [-1, -2, -3] },
            { "bSortable": false, "aTargets": [-1, -2] }
        ],
        
        // AJAX Options
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": "/api/json/evaluations/",
        "fnCreatedRow": function(row, dataArray, rowIndex) {
            var subCol = $("td", row).eq(-3), viewCol = $("td", row).eq(-2), deleteCol = $("td", row).eq(-1);
            
            subCol.html('<i class="icon-' + subCol.text() + '-sign"></i>').addClass("center");
            viewCol.html('<a href="' + viewCol.text() + '" class="btn btn-primary">View</a>').addClass("center");
            
            if (deleteCol.text() != "") {
                deleteCol.html('<form action="/deleteEvaluation/" method="POST"><input type="hidden" name="csrfmiddlewaretoken" value="' + getCookie("csrftoken") + '" /><input type="hidden" name="evaluation" value="' + deleteCol.text() + '" /><input type="submit" class="btn btn-danger prompt" data-prompt="Are you sure you want to delete this evaluation?" value="Delete" /></form>').addClass("center");
            }
        }
    });
});