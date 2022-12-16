using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Proje4
{
    class Program
    {
        public static int INFINITY = 1000;
        static void Main(string[] args)
        {
            int N = 5;
            int SRC = 0;

            Graph g = new Graph(4);

            g.AddEdge(0, 1);
            g.AddEdge(0, 2);
            g.AddEdge(1, 2);
            g.AddEdge(2, 0);
            g.AddEdge(2, 3);
            g.AddEdge(3, 3);

            Console.Write("Following is Breadth First " +
                          "Traversal(starting from " +
                          "vertex 2)\n");
            g.BFS(2);

            // int[][] cost	= new int[N][N];

            int[,] graph = new int[,] { { 0, 2, 0, 6, 0 },
                                      { 2, 0, 3, 8, 5 },
                                      { 0, 3, 0, 0, 7 },
                                      { 6, 8, 0, 0, 9 },
                                      { 0, 5, 7, 9, 0 } };

            int[,] cost = {
       { INFINITY,    5,    3, INFINITY,    2},
       { INFINITY, INFINITY,    2,    6, INFINITY},
       { INFINITY,    1, INFINITY,    2, INFINITY},
       { INFINITY, INFINITY, INFINITY, INFINITY, INFINITY},
       { INFINITY,    6,   10,    4,    INFINITY}  };

            int[] distances = new int[N];

            int[] previous = Distance(N, cost, distances, SRC);

            for (int i = 0; i < distances.Length; ++i)
                if (distances[i] != INFINITY)
                    Console.WriteLine(distances[i]);
                else Console.WriteLine("INFINITY");
        }

        public static int[] Distance(int N, int[,] cost, int[] D, int src)
        {

            int w, v, min;

            bool[] visited = new bool[N];

            int[] previous = new int[N]; //for tracking shortest paths (güzergah)

            //initialization of D[], visited[] and previous[] arrays according to src node
            for (v = 0; v < N; v++)
            {
                if (v != src)
                {
                    visited[v] = false;
                    D[v] = cost[src, v];
                    if (D[v] != INFINITY) //there is a connection between src and v
                    {
                        previous[v] = src;
                    }
                    else //no path from source
                    {
                        previous[v] = -1;
                    }
                }
                else
                {
                    visited[v] = true;
                    D[v] = 0;
                    previous[v] = -1;
                }

            }

            // Searching for shortest paths
            for (int i = 0; i < N; ++i)
            {
                min = INFINITY;
                for (w = 0; w < N; w++)
                    if (!visited[w])
                        if (D[w] < min)
                        {
                            v = w;
                            min = D[w];
                        }

                visited[v] = true;

                for (w = 0; w < N; w++)
                    if (!visited[w])
                        if (min + cost[v, w] < D[w])
                        {
                            D[w] = min + cost[v, w];
                            previous[w] = v; //update the path info
                        }
            }

            return previous;
        }

        // Number of vertices in the graph
        static int V = 5;

        // A utility function to find
        // the vertex with minimum key
        // value, from the set of vertices
        // not yet included in MST
        static int minKey(int[] key, bool[] mstSet)
        {

            // Initialize min value
            int min = int.MaxValue, min_index = -1;

            for (int v = 0; v < V; v++)
                if (mstSet[v] == false && key[v] < min)
                {
                    min = key[v];
                    min_index = v;
                }

            return min_index;
        }
        // Function to construct and
        // print MST for a graph represented
        // using adjacency matrix representation
        static void primMST(int[,] graph)
        {

            // Array to store constructed MST
            int[] parent = new int[V];

            // Key values used to pick
            // minimum weight edge in cut
            int[] key = new int[V];

            // To represent set of vertices
            // included in MST
            bool[] mstSet = new bool[V];

            // Initialize all keys
            // as INFINITE
            for (int i = 0; i < V; i++)
            {
                key[i] = int.MaxValue;
                mstSet[i] = false;
            }

            // Always include first 1st vertex in MST.
            // Make key 0 so that this vertex is
            // picked as first vertex
            // First node is always root of MST
            key[0] = 0;
            parent[0] = -1;

            // The MST will have V vertices
            for (int count = 0; count < V - 1; count++)
            {

                // Pick thd minimum key vertex
                // from the set of vertices
                // not yet included in MST
                int u = minKey(key, mstSet);

                // Add the picked vertex
                // to the MST Set
                mstSet[u] = true;

                // Update key value and parent
                // index of the adjacent vertices
                // of the picked vertex. Consider
                // only those vertices which are
                // not yet included in MST
                for (int v = 0; v < V; v++)

                    // graph[u][v] is non zero only
                    // for adjacent vertices of m
                    // mstSet[v] is false for vertices
                    // not yet included in MST Update
                    // the key only if graph[u][v] is
                    // smaller than key[v]
                    if (graph[u, v] != 0 && mstSet[v] == false
                        && graph[u, v] < key[v])
                    {
                        parent[v] = u;
                        key[v] = graph[u, v];
                    }
            }
        }
        class Graph
        {

            // No. of vertices     
            private int _V;

            //Adjacency Lists 
            LinkedList<int>[] _adj;

            public Graph(int V)
            {
                _adj = new LinkedList<int>[V];
                for (int i = 0; i < _adj.Length; i++)
                {
                    _adj[i] = new LinkedList<int>();
                }
                _V = V;
            }

            // Function to add an edge into the graph 
            public void AddEdge(int v, int w)
            {
                _adj[v].AddLast(w);

            }

            // Prints BFS traversal from a given source s 
            public void BFS(int s)
            {

                // Mark all the vertices as not
                // visited(By default set as false) 
                bool[] visited = new bool[_V];
                for (int i = 0; i < _V; i++)
                    visited[i] = false;

                // Create a queue for BFS 
                LinkedList<int> queue = new LinkedList<int>();

                // Mark the current node as 
                // visited and enqueue it 
                visited[s] = true;
                queue.AddLast(s);

                while (queue.Any())
                {

                    // Dequeue a vertex from queue 
                    // and print it
                    s = queue.First();
                    Console.Write(s + " ");
                    queue.RemoveFirst();

                    // Get all adjacent vertices of the 
                    // dequeued vertex s. If a adjacent
                    // has not been visited, then mark it 
                    // visited and enqueue it 
                    LinkedList<int> list = _adj[s];

                    foreach (var val in list)
                    {
                        if (!visited[val])
                        {
                            visited[val] = true;
                            queue.AddLast(val);
                        }
                    }
                }
            }
        }
    }

}

