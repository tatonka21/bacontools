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
            return Path.Combine(newRoot, oldPath.Replace(root, ""));
        }

        public static void PivotAndMoveFile(string oldPath, string root, string newRoot, bool overwrite = false)
        {
            if (!File.Exists(oldPath)) throw new ArgumentException("oldPath must be an existing file", "oldPath");
            string pivotedPath = PivotPath(oldPath, root, newRoot);

            if (File.Exists(pivotedPath))
            {
                if (!overwrite) return;
                File.Delete(pivotedPath);
            }

            File.Move(oldPath, pivotedPath);            
        }

    }
}
