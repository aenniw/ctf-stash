#### Challenge:

Unlucky, the flag is in Kubernetes and im not joking :/ `nc k8s.0xf.eu 8888`

Helpfull links:
- [How to use Kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
- [How to use Kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [MAYBE useful](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)

---

#### Solution:

- after connecting we list all namespaces and check permissions on resources and then we can poke around
```bash
for namespace in $(kubectl get namespaces | awk '{ print $1 }' | tail -n +2); do
  echo "Current namespace: $namespace"
  for resource in $(kubectl api-resources --verbs=list --namespaced -o name); do
    for action in get list watch create update patch delete; do
      { echo -n "- $action $resource "; kubectl auth can-i "$action" "$resource" --namespace="$namespace"; } | grep "yes"
    done
  done
done
```

- 1. part in `default` namespace secrets - `kubectl get secrets -o json -n default`
- 2. part in `secret-namespace` namespace POD logs - `kubectl logs kube-baby-flag-part2-of-3-6b97f47974-gjnk5 -n secret-namespace`
- 3. part in `secret-namespace` namespace flags `kubectl get flags.ctf.fluxfingers.hack.lu -o json -n secret-namespace`

---

<details><summary>FLAG:</summary>

```
flag{k8s_1s_r34lly_fun_but_1ts_3v3n_b3tt3r_1n_CTFS}
```

</details>
