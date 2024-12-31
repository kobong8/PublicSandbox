```mermaid
flowchart TB
    node[top node] --> node_l
    node --> node_r

    node_l --> node_ll
    node_l --> node_lr

    node_r --> node_rl
    node_r --> node_rr

    node_rl --> node_rll
    node_rl --> node_rlr
    
    node_ll --> node_lll
    node_ll --> node_llr

    node_rll --> node_rlll
    node_rll --> node_rllr
```