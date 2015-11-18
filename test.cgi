#!/opt/bin/perl
my $var = $ENV{something};
&go();
sub go {
# comment
print <<EOF;
<!DOCTYPE html>
<html>
<!-- comment -->
<script>
var foo = 'bar' // comment
</script>
</html>
EOF
}
