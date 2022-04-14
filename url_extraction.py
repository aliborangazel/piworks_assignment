access_link = "<url>https://xcd32112.smart_meter.com</url>" # an example entry in the table

xml_url_start = "<url>"
xml_url_end = "</url>"
httpTag = "http://"
httpsTag = "https://"

def extract_url(link):
    # remove the xml tags "<url>" (assuming that this tag is at the beginning of the url before the protocol) 
    # and "</url>" (assuming that this tag is at the end of the string after the url)
    if (not isinstance(link, str)): # if input is not string
        return

    xml_url_start_index = link.find(xml_url_start)
    xml_url_end_index = link.find(xml_url_end)
    # if the xml tags or protocol part are not appropriately placed
    if (xml_url_start_index == -1 or xml_url_end_index == -1):
        return

    httpTag_index = link.find(httpTag)
    httpsTag_index = link.find(httpsTag)
    # either ssl secured or normal http, if neither of the two, then return nothing
    if (httpTag_index != -1):                               # normal http
        # protocol part needs to be in between the xml tags
        if (httpTag_index < xml_url_start_index or httpTag_index > xml_url_end_index):
            return
        
        # remove xml tags and protocol part
        link = link[httpTag_index + len(httpTag) : xml_url_end_index]
        # remaining part must consists of alpha numeric chars, "_", and "." only
        for i in link:
            if (not i.isalnum() or i != '_' or i != '.'):   # unexpected character
                return
        return link

    elif (httpsTag_index != -1):                            # ssl secured http
        if (httpsTag_index < xml_url_start_index or httpsTag_index > xml_url_end_index):
            return

        # remove xml tags and protocol part
        link = link[httpsTag_index + len(httpsTag) : xml_url_end_index]
        # remaining part must consists of alpha numeric chars, "_", and "." only
        for i in link:
            if (not i.isalnum() and i != '_' and i != '.'): # unexpected character
                return
        return link

    else:                                                   # neither http not https
        return

print("\nurl : \n" + extract_url(access_link))