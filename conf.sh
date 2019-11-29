#! /usr/bin/env bash
cat > nginx.conf << EOF
server {
    listen 80;
    server_name adirect.ml www.adirect.ml;
}
EOF

#if [ ! -f /etc/nginx/nginx.conf ]; then
#    cat > /etc/nginx/nginx.conf << EOF
#    < server { >
#        listen 80;
#        server_name adirect.ml www.adirect.ml;
#    }
#EOF
#fi