pod=`kubectl get pods --namespace=tumbo --context=kubernetes-admin@kubernetes|grep ^app-|awk '{print $1}'`
for i in $(git status -s|grep tumbo|awk '{print $2}'); do
  kubectl cp $i ${pod}:./.virtualenvs/tumbo/lib/python2.7/site-packages/$i  --context=kubernetes-admin@kubernetes --namespace=tumbo 
done
kubectl exec -it ${pod} --namespace=tumbo --context=kubernetes-admin@kubernetes -- bash -c "pkill -HUP -f /home/tumbo/.virtualenvs/tumbo/bin/python"

pod=`kubectl get pods --namespace=tumbo --context=kubernetes-admin@kubernetes|grep ^background-|awk '{print $1}'`
for i in $(git status -s|grep tumbo|awk '{print $2}'); do
  kubectl cp $i ${pod}:./.virtualenvs/tumbo/lib/python2.7/site-packages/$i  --context=kubernetes-admin@kubernetes --namespace=tumbo 
done
kubectl exec -it ${pod} --namespace=tumbo --context=kubernetes-admin@kubernetes -- bash -c "pkill -HUP -f /home/tumbo/.virtualenvs/tumbo/bin/python"