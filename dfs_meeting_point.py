#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:52:27 2022

@author: angelinaxu
"""

def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        order = []
        parent[s] = s
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def find_meeting_point(Adj):
    '''
    inputs:
        Adj - an adjacency list such as [[1,2], [2], []]
    return a meeting point or None if no meeting points exist
    '''
    new_adj = [[] for i in range(len(Adj))]
    for i in range(len(Adj)):
        for elt in Adj[i]:
            new_adj[elt].append(i)
    
    parent, order = full_dfs(new_adj)
    last_num = max(order)
    for i, elt in enumerate(order):
        if elt == last_num:
            index = i
    
    parent, order = dfs(new_adj, index, parent = None, order = None)
    
    if parent.count(None) > 0:
        return None
    
    return index