# FILE INFO ###################################################
# Author: Jason Liu <liux@cis.fiu.edu>
# Created on June 14, 2019
# Last Update: Time-stamp: <2019-07-01 12:12:23 liux>
###############################################################

"""Simulation event types and event list."""

from collections.abc import MutableMapping

# ... requires the following:
#   Trap()

from .trap import *

__all__ = ["_Event", "_DirectEvent", "_ProcessEvent", "_EventList", \
           "infinite_time", "minus_infinite_time"]


# two extremes of simulation time
infinite_time = float('inf')
minus_infinite_time = float('-inf')


# PQDict is PRIORITY QUEUE DICTIONARY (PYTHON RECIPE)
# Created by Nezar Abdennur
# Python recipes (4591):
# http://code.activestate.com/recipes/578643-priority-queue-dictionary/
#
# An indexed priority queue implemented in pure python as a dict-like
# class. It is a stripped-down version of pqdict. A Priority Queue
# Dictionary maps dictionary keys (dkeys) to updatable priority keys
# (pkeys).
#
# The priority queue is implemented as a binary heap, which supports:
#       O(1) access to the top priority element
#       O(log n) removal of the top priority element
#       O(log n) insertion of a new element
#
# In addition, an internal dictionary or "index" maps dictionary keys
# to the position of their entry in the heap. This index is maintained
# as the heap is manipulated. As a result, a PQ-dict also supports:
#       O(1) lookup of an arbitrary element's priority key
#       O(log n) removal of an arbitrary element
#       O(log n) updating of an arbitrary element's priority key
# PQDict is modified to be used for our event list
 
class _MinEntry(object):
    """
    Mutable entries for a Min-PQ dictionary.

    """
    def __init__(self, dkey, pkey):
        self.dkey = dkey    #dictionary key
        self.pkey = pkey    #priority key

    def __lt__(self, other):
        return self.pkey < other.pkey

#class _MaxEntry(object):
#    """
#    Mutable entries for a Max-PQ dictionary.
#
#    """
#    def __init__(self, dkey, pkey):
#        self.dkey = dkey
#        self.pkey = pkey
#
#    def __lt__(self, other):
#        return self.pkey > other.pkey

class _PQDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._heap = []
        self._position = {}
        self.update(*args, **kwargs)

    create_entry = _MinEntry     #defaults to a min-pq

#    @classmethod
#    def maxpq(cls, *args, **kwargs):
#        pq = cls()
#        pq.create_entry = _MaxEntry
#        pq.__init__(*args, **kwargs)
#        return pq

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        for entry in self._heap:
            yield entry.dkey

    def __getitem__(self, dkey):
        return self._heap[self._position[dkey]].pkey

    def __setitem__(self, dkey, pkey):
        heap = self._heap
        position = self._position

        try:
            pos = position[dkey]
        except KeyError:
            # Add a new entry:
            # put the new entry at the end and let it bubble up
            pos = len(self._heap)
            heap.append(self.create_entry(dkey, pkey))
            position[dkey] = pos
            self._swim(pos)
        else:
            # Update an existing entry:
            # bubble up or down depending on pkeys of parent and children
            heap[pos].pkey = pkey
            parent_pos = (pos - 1) >> 1
            child_pos = 2*pos + 1
            if parent_pos > -1 and heap[pos] < heap[parent_pos]:
                self._swim(pos)
            elif child_pos < len(heap):
                other_pos = child_pos + 1
                if other_pos < len(heap) and not heap[child_pos] < heap[other_pos]:
                    child_pos = other_pos
                if heap[child_pos] < heap[pos]:
                    self._sink(pos)

    def __delitem__(self, dkey):
        heap = self._heap
        position = self._position

        pos = position.pop(dkey)
        entry_to_delete = heap[pos]

        # Take the very last entry and place it in the vacated spot. Let it
        # sink or swim until it reaches its new resting place.
        end = heap.pop(-1)
        if end is not entry_to_delete:
            heap[pos] = end
            position[end.dkey] = pos
            parent_pos = (pos - 1) >> 1
            child_pos = 2*pos + 1
            if parent_pos > -1 and heap[pos] < heap[parent_pos]:
                self._swim(pos)
            elif child_pos < len(heap):
                other_pos = child_pos + 1
                if other_pos < len(heap) and not heap[child_pos] < heap[other_pos]:
                    child_pos = other_pos
                if heap[child_pos] < heap[pos]:
                    self._sink(pos)
        del entry_to_delete

    def peek(self):
        try:
            entry = self._heap[0]
        except IndexError:
            raise KeyError
        return entry.dkey, entry.pkey

    def popitem(self):
        heap = self._heap
        position = self._position

        try:
            end = heap.pop(-1)
        except IndexError:
            raise KeyError

        if heap:
            entry = heap[0]
            heap[0] = end
            position[end.dkey] = 0
            self._sink(0)
        else:
            entry = end
        del position[entry.dkey]
        return entry.dkey, entry.pkey

    def iteritems(self):    
        # destructive heapsort iterator
        try:
            while True:
                yield self.popitem()
        except KeyError:
            return

    def _sink(self, top=0):
        # "Sink-to-the-bottom-then-swim" algorithm (Floyd, 1964)
        # Tends to reduce the number of comparisons when inserting "heavy" items
        # at the top, e.g. during a heap pop
        heap = self._heap
        position = self._position

        # Grab the top entry
        pos = top
        entry = heap[pos]
        # Sift up a chain of child nodes
        child_pos = 2*pos + 1
        while child_pos < len(heap):
            # choose the smaller child
            other_pos = child_pos + 1
            if other_pos < len(heap) and not heap[child_pos] < heap[other_pos]:
                child_pos = other_pos
            child_entry = heap[child_pos]
            # move it up one level
            heap[pos] = child_entry
            position[child_entry.dkey] = pos
            # next level
            pos = child_pos
            child_pos = 2*pos + 1
        # We are left with a "vacant" leaf. Put our entry there and let it swim 
        # until it reaches its new resting place.
        heap[pos] = entry
        position[entry.dkey] = pos
        self._swim(pos, top)

    def _swim(self, pos, top=0):
        heap = self._heap
        position = self._position

        # Grab the entry from its place
        entry = heap[pos]
        # Sift parents down until we find a place where the entry fits.
        while pos > top:
            parent_pos = (pos - 1) >> 1
            parent_entry = heap[parent_pos]
            if not entry < parent_entry:
                break
            heap[pos] = parent_entry
            position[parent_entry.dkey] = pos
            pos = parent_pos
        # Put entry in its new place
        heap[pos] = entry
        position[entry.dkey] = pos


class _Event(object):
    """The base class for all simulation events."""

    def __init__(self, time, name=None):
        self.time = time
        self.name = name
        self.trap = None

    def __str__(self):
        return "Event[%s]:%g" % (self.name if self.name else id(self), self.time)

    def __lt__(self, other):
        return self.time < other.time

    def get_trap(self, sim):
        if self.trap is None:
            self.trap = Trap(sim)
        return self.trap


class _DirectEvent(_Event):
    """The event type for direct event scheduling."""

    def __init__(self, time, func, params, name, repeat_intv):
        super(_DirectEvent, self).__init__(time, name)
        self.func = func
        self.params = params
        self.repeat_intv = repeat_intv

    def __str__(self):
        return "DirectEvent[%s]:%g%s" % \
            (self.name if self.name else id(self), self.time,
             " (repeat_intv=%d)"%self.repeat_intv if self.repeat_intv else "")

    def renew(self, time):
        self.time = time
        self.trap = None # trap cannot be reused
        return self


class _ProcessEvent(_Event):
    """The event type for process scheduling."""

    def __init__(self, time, proc, name):
        super(_ProcessEvent, self).__init__(time, name)
        self.proc = proc

    def __str__(self):
        return "ProcessEvent[%s]:%g" % (self.name, self.time)


class _EventList(object):
    """An event list sorts events in timestamp order.

    An event list is a priority queue that stores and sorts simulation
    events based on the time of the events. It supports three basic
    operations: to insert a (future) event, to peek and to retrieve
    the event with the minimal timestamp.

    """

    def __init__(self):
        #self.pqueue = []
        self.pqueue = _PQDict()
        self.last = minus_infinite_time

    def __len__(self):
        return len(self.pqueue)
        
    def insert(self, evt):
        if self.last <= evt.time:
            #heapq.heappush(self.pqueue, (evt.time, id(evt), evt))
            self.pqueue[id(evt)] = evt
        else:
            raise Exception("EventList.insert(%s): past event (last=%g)" %
                            (evt, self.last))

    def get_min(self):
        if len(self.pqueue) > 0:
            #return self.pqueue[0][0] # just return the time
            x, e = self.pqueue.peek()
            return e.time  # just return the time
        else:
            raise Exception("EventList.get_min() from empty list")

    def delete_min(self):
        if len(self.pqueue) > 0:
            #assert self.last <= self.pqueue[0][0]
            #self.last = self.pqueue[0][0]
            #return heapq.heappop(self.pqueue)[-1]
            x, e = self.pqueue.popitem()
            assert self.last <= e.time
            self.last = e.time
            return e
        else:
            raise Exception("EventList.delete_min() from empty list")

    def cancel(self, evt):
        if id(evt) not in self.pqueue:
            raise Exception("EventList.cancel(%s): event not found" % evt)
        del self.pqueue[id(evt)]

    def update(self, evt):
        if id(evt) not in self.pqueue:
            raise Exception("EventList.update(%s): event not found" % evt)
        if self.last <= evt.time:
            self.pqueue[id(evt)] = evt
        else:
            raise Exception("EventList.update(%s): past event (last=%g)" %
                            (evt, self.last))

    def current_event(self, evt):
        # check whether the event is current
        return id(evt) in self.pqueue
