$(document).ready(function()
{
	if (hash == "saved")
    {
		$("#savedNotice").fadeIn();
	}

    if (hash == "unsubmitted")
    {
        $("#unsubmittedNotice").fadeIn();
    }
	
	$(".descriptor-chosen-hidden").each(function()
    {
		if($(this).val())
        {
			$("#descriptor-" + $(this).val()).button("toggle");
		}
	});
    
    $(".descriptor-button").click(function()
    {
        var id = $(this).data("value");
        
        var header = $("#descriptor-header-" + id).text();
        var description = $.trim($("#descriptor-description-" + id).html());
        var $container = $("#descriptor-information-" + $(this).data("element"));
        
        if (description != "")
        {
            if ($container.data("autoshow") === "True")
            {
                $(".descriptor-information").not($container).slideUp();
                $(".descriptor-table-container").slideUp();
                
                $container.html("<strong>" + header + "</strong> <br /> " + description);
                
                if ($container.is(":visible") === false)
                {
                    $container.slideDown("fast");
                }
            }
        }
    });
	
    $(".descriptor-info").click(function()
    {
        var $targetTable = $(this).parent("h3").nextAll(".descriptor-table-container:first");
        
        $(".descriptor-information").slideUp();
        
        $targetTable.slideToggle();
    });
    
    $(".indicator-info").click(function(e) 
    {
        var $target = $($(this).data("target"));
        
        if($target.parent().parent().is(":visible"))
        {
            e.stopPropagation();
            $target.slideToggle("slow");
        } else
        {
            $target.delay("100").slideDown("slow");
        }
        
        e.preventDefault();
    });
    
    $(".standard-info").click(function()
    {
        $("#standards-table-container").slideToggle();
    });
    
    $(".comment-container").hide();
    
    $(".indicator-comments").click(function(e)
    {
        var $target = $($(this).data("target"));
        
        if($target.parent().parent().is(":visible"))
        {
            e.stopPropagation();
            $commentBox = $target.slideToggle("slow");
        } else
        {
            $commentBox = $target.delay("100").slideDown("slow");
        }
        
        e.preventDefault();
    });
});
