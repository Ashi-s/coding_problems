import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;


class Graph
{
    private int V;

    private LinkedList<Integer> adj[];
    int time = 0;
    static final int NIL = -1;

    Graph(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }

    void addEdge(int v, int w)
    {
        adj[v].add(w);
        adj[w].add(v);
    }

    public List<PairInt> recursiveCriticalConnectionCheck(int u, boolean visited[], int disc[],
                    int low[], int parent[], List<PairInt> list)
    {

        visited[u] = true;

        disc[u] = low[u] = ++time;

        Iterator<Integer> i = adj[u].iterator();
        while (i.hasNext())
        {
            int v = i.next();

            if (!visited[v])
            {
                parent[v] = u;
                list = recursiveCriticalConnectionCheck(v, visited, disc, low, parent, list);

                low[u] = Math.min(low[u], low[v]);

                if (low[v] > disc[u])
                    list.add(new PairInt(u, v));
            }

            else if (v != parent[u])
                low[u] = Math.min(low[u], disc[v]);
        }
        return list;
    }


    List<PairInt> findCriticalConnections()
    {
        boolean visited[] = new boolean[V];
        int disc[] = new int[V];
        int low[] = new int[V];
        int parent[] = new int[V];

        List<PairInt> list = new ArrayList<PairInt>();
        for (int i = 0; i < V; i++)
        {
            parent[i] = NIL;
            visited[i] = false;
        }

        for (int i = 0; i < V; i++)
            if (visited[i] == false)
                list = recursiveCriticalConnectionCheck(i, visited, disc, low, parent, list);
        
        List<PairInt> output = new ArrayList<PairInt>();
        for(PairInt pair: list){
            output.add(new PairInt(pair.first + 1, pair.second + 1));
        }
        return output;
    }

}


class Solution
{    
   Graph graph;
    List<PairInt> criticalConnections(int numOfServers, int numOfConnections, List<PairInt> connections){
        graph = buildGraph(numOfServers, connections);
        return graph.findCriticalConnections();
    }

    private Graph buildGraph(int numOfServers, List<PairInt> connections){
        Graph graph = new Graph(numOfServers);
        for(PairInt pair: connections){
            graph.addEdge(pair.first - 1, pair.second - 1);
        }
        return graph;
    }
}
