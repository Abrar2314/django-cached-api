Django Cached API

        This is a Django REST API project demonstrating caching to improve performance when fetching data from a database
        
        Caching implemented using Django's LocMemCache
        

Caching Method

            Backend: LocMemCache (local memory cache)

            Timeout: 5 minutes (300 seconds)

Performance Improvement

            Using caching significantly reduces the response time. 
            real    0m0.024s
            user    0m0.008s
            sys     0m0.010s
            
            With Cache (after first request)
            
            real    0m0.013s
            user    0m0.006s
            sys     0m0.004s
            Response time improved from 0.024s → 0.013s, showing caching reduces the API response time almost by half.
