// Usage: httpdf [PATH]
// Listen to an HTTP port and return free filesystem space in bytes.

package main

import (
	"flag"
	"log"
	"fmt"
	"net/http"
	"os"
	"syscall"
)

var wd string

func getspace(wd string) uint64 {
	var stat syscall.Statfs_t

	syscall.Statfs(wd, &stat)
	return stat.Bavail * uint64(stat.Bsize)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%d\n", getspace(wd))
}

func main() {
	cwd, err := os.Getwd()

	if err != nil {
		log.Fatal(err)
	}

	var port = flag.Int("port", 3000, "port to listen to")
	var path = flag.String("path", cwd, "path belonging to the watched filesystem")

	flag.Parse()

	if _, err := os.Stat(*path); os.IsNotExist(err) {
		log.Fatal("path does not exist")
	}

	wd = *path

	http.HandleFunc("/", handler)
	http.ListenAndServe(fmt.Sprintf(":%d", *port), nil)
}
