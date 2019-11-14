fields = ["id", "path"]
#filters = [ [ "project", "is", context.project ], ["id", "is", 7303 ] ]
filters = [ [ "project", "is", context.project ] ]
pf = shotgun.find("PublishedFile", filters, fields)

import os

for f in pf:
    path = f.get("path").get("local_path_windows")
    try:
        os.rename(f.get("path").get("local_path_windows"), f.get("path").get("local_path_windows").replace("_v0", ".v0"))
        data = {
        "path": {
            "local_path": f.get("path").get("local_path_windows").replace("_v0", ".v0"),
            "local_path_windows": f.get("path").get("local_path_windows").replace("_v0", ".v0")
        } }
        res = shotgun.update("PublishedFile", f["id"], data)
        print " "
        print "Renamed and repathed file:"
        print res
    except:
        print " "
        print "Could not repath file:"
        print path
