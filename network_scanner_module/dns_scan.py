import dns.resolver

answers = dns.resolver.query('google.com', 'A')
for rdata in answers:
    print(rdata)
