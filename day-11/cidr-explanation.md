
# CIDR (Classless Inter-Domain Routing)

CIDR, or Classless Inter-Domain Routing, is a method for allocating IP addresses and routing Internet Protocol packets. It was introduced in 1993 to replace the older system based on classes A, B, and C.

## Key Concepts

### 1. CIDR Notation
CIDR notation specifies an IP address and the associated network mask. It is written as:

```
IP_address/prefix_length
```

Example:
```
192.168.1.0/24
```

Here:
- `192.168.1.0` is the network address.
- `/24` means that the first 24 bits are the network portion, leaving the remaining bits for host addresses.

### 2. Subnetting with CIDR
CIDR allows for more efficient allocation of IP addresses compared to the traditional classful addressing system.

Example:
- A /24 network (255.255.255.0) provides 256 IP addresses.
- A /26 network (255.255.255.192) provides 64 IP addresses.

This flexibility helps prevent IP address exhaustion.

### 3. Supernetting
CIDR can also combine several IP networks into a single routing table entry, a process known as *supernetting*. This helps reduce the size of routing tables and improves routing efficiency.

Example:
```
192.168.0.0/23
```
This covers two class C networks: `192.168.0.0` to `192.168.1.255`.

## Benefits of CIDR
- Reduces IP address waste
- Simplifies routing tables
- Supports route aggregation (supernetting)

## Use in Routing
Routers use CIDR to determine how to forward packets. A router matches the destination IP address with the most specific CIDR route available (longest prefix match).

---

CIDR is a fundamental part of modern IP networking, making efficient use of IPv4 and IPv6 address spaces.
