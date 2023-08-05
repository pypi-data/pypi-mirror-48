/* colgraphweb.js */

options = {
    "interaction": {"hover": true},
	"manipulation": {"enabled": false},
    "configure": {"enabled": false},
    "edges": {
        "color": {"inherit": true},
        "smooth": {
            "enabled": false,
            "type": "continuous"
         }
    },
    "nodes": {
        "shape": "dot"
    },
    "interaction": {
        "hover": true,
        "dragNodes": true,
        "hideEdgesOnDrag": false,
        "hideNodesOnDrag": false
    },
    "physics": {
        "barnesHut": {
            "avoidOverlap": 0,
            "centralGravity": 0.5,
            "damping": 0.09,
            "gravitationalConstant": -80000,
            "springConstant": 0.001,
            "springLength": 250
        },
        "enabled": true,
        "stabilization": {
            "enabled": true,
            "fit": true,
            "iterations": 100,
            "onlyDynamicEdges": false,
            "updateInterval": 10
        }
    }
};


// same options for now
bgoptions = mcgoptions = cgoptions = options;


function makebg() {
    bgcontainer = document.getElementById('bgcontainer');
    bgdata = {
        nodes: bgnodes,
        edges: bgedges
    };
    // create a basegraph
    basegraph = new vis.Network(bgcontainer, bgdata, bgoptions);
    basegraph.setOptions({"manipulation": {"enabled": true}});
    return basegraph;
}

function makecg() {
    cgcontainer = document.getElementById('cgcontainer');
    cgdata = {
        nodes: cgnodes,
        edges: cgedges
    };
    // create a coloringgraph
    coloringgraph = new vis.Network(cgcontainer, cgdata, cgoptions);
    
    /*
    coloringgraph.on("stabilizationProgress", function(params) {
            document.getElementById('loadingBar').removeAttribute("style");
            var maxWidth = cgcontainer.width;
            var minWidth = 1;
            var widthFactor = params.iterations/params.total;
            var width = Math.max(minWidth,maxWidth * widthFactor);

            document.getElementById('bar').style.width = width + 'px';
            document.getElementById('text').innerHTML = Math.round(widthFactor*100) + '%';
        });
    coloringgraph.once("stabilizationIterationsDone", function() {
            document.getElementById('text').innerHTML = '100%';
            document.getElementById('bar').style.width = cgcontainer.width;//'496px';
            document.getElementById('loadingBar').style.opacity = 0;
            // really clean the dom element
            setTimeout(function () {document.getElementById('loadingBar').style.display = 'none';}, 500);
    });*/

    return coloringgraph;
}

function makemcg() {
    mcgcontainer = document.getElementById('mcgcontainer');
    mcgdata = {
        nodes: mcgnodes,
        edges: mcgedges
    };
    // create a metagraph
    metacoloringgraph = new vis.Network(mcgcontainer, mcgdata, mcgoptions);
    return metacoloringgraph;
}

basegraph = makebg();
coloringgraph = makecg();
metacoloringgraph = makemcg();


function objectToArray(obj) {
    return Object.keys(obj).map(function (key) {
      obj[key].id = key;
      return obj[key];
    });
}

function exportNetwork(network) {

    // function addConnections(elem, index) {
    //     elem.connections = network.getConnectedNodes(index);
    // }

    var nodes = objectToArray(network.getPositions());
    for (var ix = 0; ix < nodes.length; ix++) {
        nodes[ix]["connections"] = network.getConnectedNodes(nodes[ix]["id"]);
    }
    postdata = [
        nodes,
        document.getElementById('numcolors-textfield').value
    ]
    var exportValue = JSON.stringify(postdata, undefined, 2);

    return exportValue;
}

function generate(e) {
    // e.preventDefault();
    var value = exportNetwork(basegraph);
    $.ajax({
        type: "POST",
        url: "/",
        data: value,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (response) {
            // alert('RESPONSE OK');
            var cgcontainer = $('#cgcontainer');
            cgcontainer.html(response['cgcontainer']);
            makecg();
            var mcgcontainer = $('#mcgcontainer');
            mcgcontainer.html(response['mcgcontainer']);
            makemcg();
        },
        error: function (response) {
            alert('ERROR', response);
        }
    });
    // location.reload();
}
