"""
Knowledge Graph Application - Flask Backend
M.Tech AIML - NLP Applications
Assignment 1 - PS-9

This application manages a transportation network knowledge graph
using NetworkX and provides a web interface for visualization.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import networkx as nx
import json
import csv
import io
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize the knowledge graph
G = nx.DiGraph()

# Store relationship history for querying
relationship_history = []


@app.route('/')
def index():
    """Render the main application page"""
    return render_template('index.html')


@app.route('/api/add_relationship', methods=['POST'])
def add_relationship():
    """
    Add a new entity-relationship-entity triple to the knowledge graph

    Expected JSON format:
    {
        "entity1": "City A",
        "relationship": "connected_by_train",
        "entity2": "City B"
    }
    """
    try:
        data = request.get_json()
        entity1 = data.get('entity1', '').strip()
        relationship = data.get('relationship', '').strip()
        entity2 = data.get('entity2', '').strip()

        # Validate input
        if not entity1 or not relationship or not entity2:
            return jsonify({
                'success': False,
                'message': 'All fields (entity1, relationship, entity2) are required'
            }), 400

        # Add edge to graph with relationship as edge attribute
        G.add_edge(entity1, entity2, relationship=relationship)

        # Store in history
        relationship_history.append({
            'entity1': entity1,
            'relationship': relationship,
            'entity2': entity2,
            'timestamp': datetime.now().isoformat()
        })

        return jsonify({
            'success': True,
            'message': f'Added relationship: {entity1} --[{relationship}]--> {entity2}',
            'graph_stats': {
                'nodes': G.number_of_nodes(),
                'edges': G.number_of_edges()
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error adding relationship: {str(e)}'
        }), 500


@app.route('/api/upload_csv', methods=['POST'])
def upload_csv():
    """
    Upload CSV file with bulk entity-relationship data

    Expected CSV format:
    entity1,relationship,entity2
    Mumbai,connected_by_train,Delhi
    Delhi,has_airport,IGI Airport
    """
    try:
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'message': 'No file uploaded'
            }), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({
                'success': False,
                'message': 'No file selected'
            }), 400

        if not file.filename.endswith('.csv'):
            return jsonify({
                'success': False,
                'message': 'File must be a CSV file'
            }), 400

        # Read CSV file
        stream = io.StringIO(file.stream.read().decode("UTF-8"), newline=None)
        csv_reader = csv.DictReader(stream)

        added_count = 0
        errors = []

        for row_num, row in enumerate(csv_reader, start=2):
            try:
                entity1 = row.get('entity1', '').strip()
                relationship = row.get('relationship', '').strip()
                entity2 = row.get('entity2', '').strip()

                if entity1 and relationship and entity2:
                    G.add_edge(entity1, entity2, relationship=relationship)
                    relationship_history.append({
                        'entity1': entity1,
                        'relationship': relationship,
                        'entity2': entity2,
                        'timestamp': datetime.now().isoformat()
                    })
                    added_count += 1
                else:
                    errors.append(f'Row {row_num}: Missing required fields')

            except Exception as e:
                errors.append(f'Row {row_num}: {str(e)}')

        response = {
            'success': True,
            'message': f'Successfully added {added_count} relationships',
            'added_count': added_count,
            'graph_stats': {
                'nodes': G.number_of_nodes(),
                'edges': G.number_of_edges()
            }
        }

        if errors:
            response['warnings'] = errors

        return jsonify(response)

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error processing CSV: {str(e)}'
        }), 500


@app.route('/api/query', methods=['POST'])
def query_graph():
    """
    Query the knowledge graph for relationships

    Supported query types:
    - Find all relationships of an entity
    - Find path between two entities
    - Find neighbors of an entity
    """
    try:
        data = request.get_json()
        query_type = data.get('query_type', 'neighbors')
        entity = data.get('entity', '').strip()

        if not entity:
            return jsonify({
                'success': False,
                'message': 'Entity is required for query'
            }), 400

        if entity not in G.nodes():
            return jsonify({
                'success': False,
                'message': f'Entity "{entity}" not found in graph'
            }), 404

        results = {}

        if query_type == 'neighbors':
            # Find all neighbors (both incoming and outgoing)
            successors = list(G.successors(entity))
            predecessors = list(G.predecessors(entity))

            # Get relationships
            outgoing = []
            for succ in successors:
                rel = G[entity][succ].get('relationship', 'related_to')
                outgoing.append({
                    'entity': succ,
                    'relationship': rel,
                    'direction': 'outgoing'
                })

            incoming = []
            for pred in predecessors:
                rel = G[pred][entity].get('relationship', 'related_to')
                incoming.append({
                    'entity': pred,
                    'relationship': rel,
                    'direction': 'incoming'
                })

            results = {
                'entity': entity,
                'outgoing_relationships': outgoing,
                'incoming_relationships': incoming,
                'total_connections': len(successors) + len(predecessors)
            }

        elif query_type == 'path':
            target = data.get('target', '').strip()

            if not target:
                return jsonify({
                    'success': False,
                    'message': 'Target entity is required for path query'
                }), 400

            if target not in G.nodes():
                return jsonify({
                    'success': False,
                    'message': f'Target entity "{target}" not found in graph'
                }), 404

            try:
                # Find shortest path
                path = nx.shortest_path(G, entity, target)

                # Get relationships along the path
                path_with_relationships = []
                for i in range(len(path) - 1):
                    rel = G[path[i]][path[i+1]].get('relationship', 'related_to')
                    path_with_relationships.append({
                        'from': path[i],
                        'relationship': rel,
                        'to': path[i+1]
                    })

                results = {
                    'source': entity,
                    'target': target,
                    'path': path,
                    'path_length': len(path) - 1,
                    'path_details': path_with_relationships
                }

            except nx.NetworkXNoPath:
                results = {
                    'source': entity,
                    'target': target,
                    'path': None,
                    'message': f'No path found between {entity} and {target}'
                }

        elif query_type == 'all_relationships':
            # Get all relationships involving this entity
            relationships = []

            for pred in G.predecessors(entity):
                rel = G[pred][entity].get('relationship', 'related_to')
                relationships.append({
                    'entity1': pred,
                    'relationship': rel,
                    'entity2': entity
                })

            for succ in G.successors(entity):
                rel = G[entity][succ].get('relationship', 'related_to')
                relationships.append({
                    'entity1': entity,
                    'relationship': rel,
                    'entity2': succ
                })

            results = {
                'entity': entity,
                'relationships': relationships,
                'count': len(relationships)
            }

        return jsonify({
            'success': True,
            'results': results
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error executing query: {str(e)}'
        }), 500


@app.route('/api/graph', methods=['GET'])
def get_graph():
    """
    Get the complete graph data for visualization

    Returns nodes and edges in format compatible with Vis.js
    """
    try:
        # Prepare nodes
        nodes = []
        for node in G.nodes():
            nodes.append({
                'id': node,
                'label': node,
                'title': f'Entity: {node}'  # Tooltip
            })

        # Prepare edges
        edges = []
        for i, (source, target, data) in enumerate(G.edges(data=True)):
            relationship = data.get('relationship', 'related_to')
            edges.append({
                'id': i,
                'from': source,
                'to': target,
                'label': relationship,
                'title': relationship,  # Tooltip
                'arrows': 'to'
            })

        return jsonify({
            'success': True,
            'graph': {
                'nodes': nodes,
                'edges': edges
            },
            'stats': {
                'node_count': len(nodes),
                'edge_count': len(edges)
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving graph: {str(e)}'
        }), 500


@app.route('/api/clear_graph', methods=['POST'])
def clear_graph():
    """Clear all data from the graph"""
    global G, relationship_history

    try:
        G.clear()
        relationship_history.clear()

        return jsonify({
            'success': True,
            'message': 'Graph cleared successfully'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error clearing graph: {str(e)}'
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get graph statistics"""
    try:
        stats = {
            'nodes': G.number_of_nodes(),
            'edges': G.number_of_edges(),
            'density': nx.density(G) if G.number_of_nodes() > 0 else 0,
            'is_connected': nx.is_weakly_connected(G) if G.number_of_nodes() > 0 else False,
            'total_relationships': len(relationship_history)
        }

        return jsonify({
            'success': True,
            'stats': stats
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error getting stats: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
