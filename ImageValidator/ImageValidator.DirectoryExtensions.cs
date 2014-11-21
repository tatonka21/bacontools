using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ImageValidator
{
    public static class DirectoryExtensions
    {
        public static string PivotPath(string oldPath, string root, string newRoot)
        {
            DirectoryInfo di = new DirectoryInfo(newRoot);

            return di.FullName + oldPath.Replace(root, "");
        }

        public static void PivotMoveFile(string oldPath, string root, string newRoot, bool overwrite = false)
        {
            // Console.WriteLine("PivotMoveFile {0}, {1}, {2}", oldPath, root, newRoot);

            if (!File.Exists(oldPath)) throw new ArgumentException("oldPath must be an existing file", "oldPath");
            string pivotedPath = PivotPath(oldPath, root, newRoot);

            if (File.Exists(pivotedPath))
            {
                if (!overwrite) return;
                File.Delete(pivotedPath);
            }

            // Console.WriteLine("Moving {0} >> {1}", oldPath, pivotedPath);

            File.Move(oldPath, pivotedPath);            
        }

        public static void PivotCopyFile(string oldPath, string root, string newRoot, bool overwrite = false)
        {
            // Console.WriteLine("PivotCopyFile {0}, {1}, {2}", oldPath, root, newRoot);

            if (!File.Exists(oldPath)) throw new ArgumentException("oldPath must be an existing file", "oldPath");
            string pivotedPath = PivotPath(oldPath, root, newRoot);

            // Console.WriteLine("Copying {0} >> {1}", oldPath, pivotedPath);

            DirectoryInfo di = new DirectoryInfo(pivotedPath);
            string diroot = di.Parent.FullName;
            // Console.WriteLine(diroot);
            if (!Directory.Exists(diroot)) Directory.CreateDirectory(diroot);

            File.Copy(oldPath, pivotedPath, overwrite);
        }

        public static void MoveFile (string fname, string destination, bool overwrite = false)
        {
            DirectoryInfo di = new DirectoryInfo(destination);
            FileInfo fi = new FileInfo(fname);
            string dest = di.FullName + '\\' + fi.Name;

            if (!new DirectoryInfo(dest).Parent.Exists) Directory.CreateDirectory(new DirectoryInfo(dest).Parent.FullName);

            // Console.WriteLine("MoveFile {0} >> {1}", fname, dest);

            if (!File.Exists(fname)) {throw new ArgumentException("fname must be an existing file", "fname");  }
            else if (File.Exists(dest))
            {
                if (overwrite) { File.Delete(dest); } else return;
            }
            File.Move(fname, dest);
        }

        public static void CopyFile (string fname, string destination, bool overwrite = false)
        {
            DirectoryInfo di = new DirectoryInfo(destination);
            FileInfo fi = new FileInfo(fname);
            string dest = di.FullName + '\\' + fi.Name;

            //Console.WriteLine("CopyFile {0} >> {1}", fname, dest);

            if (!new DirectoryInfo(dest).Parent.Exists) Directory.CreateDirectory(new DirectoryInfo(dest).Parent.FullName);

            if (!File.Exists(fname)) {throw new ArgumentException("fname must be an existing file", "fname");  }
            else if (File.Exists(dest))
            {
                if (overwrite) {File.Delete(dest);} else return;
            }
            File.Copy(fname, dest, false);
        }

    }
}
