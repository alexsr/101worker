from repo import Repo
import detection
import getpass
import json
import sys
import subprocess
from termcolor import colored
import pysftp

def set_worker(reponame, contribname, sha):
  print "Preparing worker for commit " + colored(sha, 'magenta')
  subprocess.Popen(["git", "checkout " + sha], cwd="../../../101results/gitdeps/" + reponame, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  print "> " + colored(contribname, 'cyan')
  subprocess.Popen(["rm", "-rf", contribname], cwd="../../../101results/101repo/contributions/" + reponame, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  subprocess.Popen(["cp", "-r", "../../../101results/gitdeps/" + reponame + "/contributions/" + contribname, "../../../101results/101repo/contributions/"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def detect(request):
  reponame = request.GET.get('reponame', '').split('/')[0]
  contribname = request.GET.get('contribname', '').split('/')[0]
  sha = request.GET.get('sha', '').split('/')[0]
  repo = Repo("101companies", reponame)
  set_worker(reponame, contribname, sha)
  features = detection.detect_all(contribname, sha)
  set_worker(reponame, contribname, 'master')
  return HttpResponse(features, content_type='text/json')



