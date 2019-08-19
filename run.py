'''
# ppl-proper/run.py - dev server
'''
from pplproper import app

app.run(host="0.0.0.0", port=5006, debug=True, processes=5, threaded=False)


# app.run(host="0.0.0.0", port=5006, debug=True, processes=5, threaded=False,
#         ssl_context=("/etc/pki/tls/private/meshinprod12.parc.com.pem",
#                      "/etc/pki/tls/private/meshinprod12.parc.com.key"))
