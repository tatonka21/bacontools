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
            Console.WriteLine(diroot);
            if (!Directory.Exists(diroot)) Directory.CreateDirectory(diroot);

            File.Copy(oldPath, pivotedPath, overwrite);
        }

    }
}
