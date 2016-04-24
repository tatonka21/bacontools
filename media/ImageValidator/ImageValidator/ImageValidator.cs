using System;
using System.Collections.Generic;
using System.Linq;
using System.Drawing;
using System.IO;

namespace ImageValidator
{
    internal static class ImageValidator
    {
        internal static TextWriter CorruptedFileListOutput = Console.Out;
        internal static TextWriter ProgressReportOutput = Console.Out;

        internal static Options Opts;

        private static int Processed = 0;
        private static int FailedImages = 0;
        internal static bool ProgressTrack = true;

        internal static object Locker = new object();
        internal static readonly string[] ValidImageExtensions = { "jpg", "jpeg", "bmp", "gif", "png" };

        static ImageValidator()
        {
        }

        internal static void ProcessImages(IEnumerable<string> images, Action<string> OnFail)
        {
            int expectedTotal = images.Count();

            images.AsParallel().ForAll(s =>
                {
                    ProcessImage(s, OnFail);
                    if (++Processed % Opts.LogPeriod == 0) ReportProgress(expectedTotal);
                });
        }

        private static void ProcessImage(string imagePath, Action<string> OnFail)
        {
            IDisposable img = new ImageStub();

            try
            {
                img = Image.FromFile(imagePath);
            }
            catch (Exception e)
            {
                lock (Locker)
                {
                    CorruptedFileListOutput.WriteLine("{0}{1}", imagePath, Opts.Verbose ? ":" + e.Message : "");
                    FailedImages++;
                }

                OnFail(imagePath);
            }
            finally
            {
                img.Dispose();
            }
        }

        private static void ReportProgress(int max)
        {
            ProgressReportOutput.WriteLine("{0}/{1} completed; {2} failed to load", Processed, max, FailedImages);
        }

        internal static bool IsValidImagePath(string path)
        {
            return path.ToLowerInvariant().EndsWithAny(ValidImageExtensions);
        }

        internal static bool EndsWithAny(this string source, IEnumerable<string> elements)
        {
            return elements.Any(s => source.EndsWith(s));
        }

        internal static bool EndsWithAny(this string source, params string[] elements)
        {
            return source.EndsWithAny((IEnumerable<string>)elements);
        }

        internal static bool StartsWithAny(this string source, IEnumerable<string> elements)
        {
            return elements.Any(s => source.StartsWith(s));
        }

        internal static bool StartsWithAny(this string source, params string[] elements)
        {
            return source.StartsWithAny((IEnumerable<string>)elements);
        }

        internal static bool ContainsAny<T>(this IEnumerable<T> source, IEnumerable<T> elements)
        {
            return elements.Any(s => elements.Contains(s));
        }

        internal static bool ContainsAny<T>(this IEnumerable<T> source, params T[] elements)
        {
            return source.ContainsAny((IEnumerable<T>)elements);
        }

        private class ImageStub : IDisposable { public void Dispose(){} };
    }
}