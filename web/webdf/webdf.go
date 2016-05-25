package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"
	"syscall"
)

func getspace() uint64 {
	var stat syscall.Statfs_t
	wd, _ := os.Getwd()
	syscall.Statfs(wd, &stat)
	return stat.Bavail * uint64(stat.Bsize)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%d\n", getspace())
}

func main() {
	var port = flag.Int("port", 3000, "port to listen to")
	flag.Parse()

	http.HandleFunc("/", handler)
	http.ListenAndServe(fmt.Sprintf(":%d", *port), nil)
}
